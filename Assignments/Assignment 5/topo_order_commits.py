#!/usr/local/cs/bin/python3
import os
import sys
import zlib
from collections import deque

#  I tested this using this strace command:
#       strace -f -e execve ./topo_order_commits.py
#  The trace showed no invocations of git or other shell commands:
# execve("./topo_order_commits.py", ["./topo_order_commits.py"],
# 0x7ffd388754f8 /* 60 vars */) = 0


class CommitNode:
    def __init__(self, commit_hash):
        """
        :type commit_hash: str
        """
        self.commit_hash = commit_hash
        self.parents = set()
        self.children = set()


def get_git_dir():

    # set the current directory
    cdir = os.getcwd()

    # walk upwards through the filsystem until a directory with name ".git" is
    # found. Return the absoloute path.
    while True:
        if os.path.dirname(cdir) == cdir:
            break
        cfiles = os.listdir(cdir)
        for f in cfiles:
            if f == ".git":
                return cdir
        cdir = os.path.dirname(cdir)

    # if we've reached the root folder and no .git has been found, output to
    # standard error
    sys.stderr.write("Not inside a Git repository\n")
    sys.exit(1)


def get_branches(path):

    # set the directory for the branches in the git path
    bdir = os.path.join(path, "refs", "heads")

    # dictionary of branch names and their head hash
    branch_hash = dict()

    # if there are no branches, return the empty dictionary
    if not os.path.isdir(bdir):
        return branch_hash

    # walk through the directory, including branches with slashes in their name
    for root, _, files in os.walk(bdir):
        for name in files:
            bpath = os.path.join(root, name)
            branch = os.path.relpath(bpath, bdir).replace(os.sep, "/")
            with open(bpath, 'r') as f:
                branch_hash[branch] = f.read().strip()

    return branch_hash


def read_git_object(gitdir, hash):

    # object path is determined by going into the .git/objects/[]/[], where
    # []/[] is the appropiate value from the given hash
    opath = os.path.join(gitdir, 'objects', hash[:2], hash[2:])

    # if this object does not exists or is a directory, return nothing
    if not os.path.exists(opath) or os.path.isdir(opath):
        return None

    # open this file and read it with zlib into data
    with open(opath, 'rb') as f:
        data = zlib.decompress(f.read())

    # return the content after the null byte, decoded into utf-8 for
    # readability and easier parsing later on
    content = data[data.index(b'\x00') + 1:]
    return content.decode('utf-8')


def get_parents_from_git_object(object):

    # from an object (decoded utf-8), split it into lines
    lines = object.split('\n')

    # set of unique hashes (parents) of the current object
    parents = set()

    # loop through lines until we find lines that specify a parent. add the
    # hash after 'parent ' to the set. terminate after 'author' as that comes
    # after parents are listed
    for line in lines:
        if line.startswith('parent '):
            parents.add(line[7:])
        if line.startswith('author '):
            break

    # return parents if they exist
    return parents

# create a node from a given object and its hash


def create_node_from_object(object, hash):
    node = CommitNode(hash)
    node.parents = get_parents_from_git_object(object)
    return node

# iteratively search [recursive gave me errors :(] through each branch to
# find all reachable commits.


def search_branch(gitdir, head, seen, nodes):
    stack = [head]

    while stack:
        hash = stack.pop()

        # Skip commits already visited
        if hash in seen:
            continue
        seen.add(hash)

        # Read and decompress the Git object content for the current commit
        content = read_git_object(gitdir, hash)
        # Skip if object not found or invalid
        if content is None:
            continue

        # Create a node if it doesn't exist yet, else retrieve existing node
        if hash not in nodes:
            node = create_node_from_object(content, hash)
            nodes[hash] = node
        else:
            node = nodes[hash]

        # Iterate over parents to build the graph connections
        for parent_hash in node.parents.copy():
            # Create parent node if missing
            if parent_hash not in nodes:
                parent_content = read_git_object(gitdir, parent_hash)
                if parent_content is None:
                    continue
                parent_node = create_node_from_object(
                    parent_content, parent_hash)
                nodes[parent_hash] = parent_node
            else:
                parent_node = nodes[parent_hash]

            # Ensure both parent and child link to each other
            node.parents.add(parent_hash)
            parent_node.children.add(hash)

            # Schedule parent for DFS if not yet visited
            if parent_hash not in seen:
                stack.append(parent_hash)

# use khan's algorithm to topographically sort all nodes from all branches


def topo_sort_nodes(all_nodes):

    # Initialize in-degree count (number of incoming edges) for each node
    in_degree = {h: 0 for h in all_nodes}
    for node in all_nodes.values():
        for child_hash in node.children:
            in_degree[child_hash] += 1

    # Start with nodes that have no incoming edges (in-degree 0)
    queue = deque([h for h, deg in in_degree.items() if deg == 0])
    topo_order = []

    # Process nodes in queue until empty
    while queue:
        current = queue.popleft()
        topo_order.append(current)

        # For each child, reduce its in-degree since parent is processed
        for child_hash in all_nodes[current].children:
            in_degree[child_hash] -= 1
            # If child's in-degree drops to zero, enqueue it for processing
            if in_degree[child_hash] == 0:
                queue.append(child_hash)

    # Check if all nodes were processed; if not, there's a cycle or missing
    # commits
    if len(topo_order) != len(all_nodes):
        sys.stderr.write("Cycle detected or missing commits\n")
        sys.exit(1)

    return topo_order

# print commit graph as specified in the spec


def print_commit_log(topo_sorted, all_nodes, branch_heads):
    # Map each commit hash to the branches pointing to it
    commit_to_branches = {}
    for name, h in branch_heads.items():
        commit_to_branches.setdefault(h, []).append(name)

    # Reverse order so newest commits appear first
    topo_sorted = topo_sorted[::-1]
    printed_hashes = set()
    i = 0
    new_segment = False

    while i < len(topo_sorted):
        curr = topo_sorted[i]
        node = all_nodes[curr]

        # If starting a new segment after a break, print children of previous
        # commit
        if new_segment:
            children = sorted(node.children)
            print("={}".format(" ".join(children)))
            new_segment = False

        # Prepare line with commit hash
        line = curr
        # Append branch names if this commit is a branch head
        if curr in commit_to_branches:
            branches = sorted(commit_to_branches[curr])
            line += " " + " ".join(branches)
        print(line)
        printed_hashes.add(curr)

        # Check if next commit is a parent of current commit, else start new
        # segment
        if i + 1 < len(topo_sorted):
            next_commit = topo_sorted[i + 1]
            if next_commit not in node.parents:
                # Sticky end: print parents of current commit and equals sign
                parent_line = sorted(node.parents)
                print(" ".join(parent_line) + " =")
                print()
                new_segment = True
        i += 1


def topo_order_commits():
    # get the git directory path
    gitdir = os.path.join(get_git_dir(), ".git")
    # get the local branches
    local_branches = get_branches(gitdir)

    all_nodes = {}
    # for each branch, iterative DFS to find reachable nodes
    for branch_head in local_branches.values():
        seen = set()
        search_branch(gitdir, branch_head, seen, all_nodes)

    # topographically sort all nodes
    topo_sorted = topo_sort_nodes(all_nodes)

    # print graph
    print_commit_log(topo_sorted, all_nodes, local_branches)


if __name__ == "__main__":
    topo_order_commits()
