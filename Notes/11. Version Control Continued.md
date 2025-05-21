# Git: Version Control Case Study

## 1. Introduction to Version Control and Git

Git is a distributed version control system that manages files and tracks changes, providing capabilities for branching, merging, committing, and collaboration. It allows you to view both your "past" via the object database and your "planned future" via the index (also called the cache or staging area).

---

## 2. Git's Three States

### 2.1 Working Directory/Files
The “working files” refer to the actual files that a developer edits. These are visible to compilers, test programs, and other development tools.

### 2.2 Index (aka Cache/Staging Area)
Represents the planned future. Files added to the staging area are those scheduled for the next commit. You use `git add` to move files here.

### 2.3 Object Database (History)
Contains all committed snapshots of your project. These commits are immutable. You use `git log` to view this history.

---

## 3. Viewing Differences with git diff

Git provides various ways to compare different snapshots:

| Command               | Comparison                             | Description                                                              |
|----------------------|-----------------------------------------|--------------------------------------------------------------------------|
| `git diff`           | Working directory vs. staged changes    | Shows modifications in working files not yet staged                      |
| `git diff --cached`  | Staged changes vs. last commit (HEAD)   | Shows the difference between the staged version and the last commit      |
| `git diff HEAD`      | Working directory vs. last commit       | Shows all changes in working files compared to last commit               |
| `git diff <commit>`  | Working files vs. specific commit       | Useful for comparing changes with a chosen past commit                   |

Note: `HEAD` refers symbolically to the most recent commit.

To find commit hashes use:

```bash
git log
```

This lists commits in reverse chronological order with metadata including author and commit ID.

---

## 4. Committing Changes

### 4.1 Adding Changes
```bash
git add filename
```
Stages the file (adds to the index) for the next commit.

### 4.2 Making a Commit
```bash
git commit
```
This opens an editor requesting a commit message. Describe:

- What the change is.
- Why the change was made.

### 4.3 Ideal Commit Messages
Should be meaningful, not left empty or generic (e.g., "xyz"). Explain the *reason* for change, not just what changed.

Some projects enforce message format using commit hooks (example: Diffutils).

### 4.4 Hooks and Rejected Commits
Hooks such as commit message format checkers may reject commits if message syntax does not match the project’s required format.

---

## 5. Commit Hashes and Checksums

### 5.1 SHA-1 as Commit IDs
Git uses SHA-1, a 160-bit cryptographic hash function, to generate commit IDs. The hash:

- Is uniquely tied to contents and metadata of the commit.
- Provides immutability — changing contents results in a new ID.

### 5.2 Collision Probability
Due to SHA-1's large bit length, the probability of accidental collision (two different commits with same ID) is astronomically low.

### 5.3 Metadata Included in Hash
The contents of a commit include:

- Source code snapshot
- Author
- Date/time
- Commit message
- Parent commit ID(s)

Changing any part alters the SHA-1, resulting in a new commit ID.

---

## 6. Amending Commits

```bash
git commit --amend
```
Allows you to correct the most recent commit by replacing it with a new one.

### 6.1 Use Cases
- Fix minor mistakes
- Update messages
- Add forgotten changes

### 6.2 Caution
Important for beginner users to avoid obsessing over perfection. Be comfortable accumulating commits naturally even if they contain small mistakes.

---

## 7. Convenience Features

### 7.1 Committing All Changes
```bash
git commit -a -m "message"
```
The `-a` flag tells Git to automatically stage all tracked, modified files before committing. The `-m` flag lets you specify the commit message inline.

### 7.2 Viewing Tracked Files
```bash
git ls-files
```
Lists all files tracked under Git.

### 7.3 Searching Content

```bash
git grep 'pattern'
```
Efficiently searches tracked files for a pattern.

Or use:

```bash
git ls-files | xargs grep 'pattern'
```
Same result, but uses standard shell tools.

---

## 8. Git Status and Untracked Files

```bash
git status
```
Shows:

- Modified files
- Staged files
- Untracked files (not in Git or .gitignore)

---

## 9. Ignoring Files with .gitignore

`.gitignore` specifies patterns of files to ignore in Git repositories.

### 9.1 Examples

| Pattern             | Meaning                                                |
|---------------------|--------------------------------------------------------|
| `*.o`               | Ignore object files in any directory                   |
| `/main.mk`          | Ignore only at repository root                         |
| `build/`            | Ignore entire directory `build` and its contents       |

### 9.2 Sources
This file is versioned and included in the repository because it tells collaborators what not to track.

### 9.3 Multiple .gitignore Files
You can place `.gitignore` files in any directory. Git checks the closest one first.

---

## 10. Git Configuration

Contained in:
```bash
.git/config
```

Stores repository-specific settings including core options, branches, remotes, etc.

### 10.1 View with:
```bash
git config -l
```

### 10.2 Modify with:

```bash
git config <key> <value>
```

Use caution when editing `.git/config` directly, and back it up before changing.

---

## 11. Commit Reference Syntax

### 11.1 Shorthand for Commit IDs

| Syntax             | Meaning                                                |
|--------------------|--------------------------------------------------------|
| `HEAD`             | Latest commit on current branch                        |
| `HEAD^`            | First parent (one commit back)                         |
| `HEAD^^`           | Two commits back                                       |
| `HEAD~3`           | Three commits back (alternative)                       |
| `commit^2`         | In merges, refers to the second parent                 |
| `HEAD^!` or `commit^!` | Difference between current commit and its parent   |

### 11.2 Use Cases

```bash
git log HEAD^!
git diff HEAD~1
git diff HEAD^^ -- file.c
git diff HEAD -- file.txt
```

To avoid ambiguity with filenames, use:
```bash
git diff HEAD -- file.c
```

---

## 12. git blame

Displays the last commit that modified each line of a file.

```bash
git blame filename
```

### 12.1 Caution
- Not always useful for identifying the *real* cause of bugs.
- Blame shouldn’t be used to punish individual developers.
- Developers may avoid writing meaningful commits to avoid blame.

### 12.2 Use to Trace Bugs

1. Use `git blame` to identify which commit changed a line.
2. Use `git diff <commit>^!` to view the change.

Blame is helpful for understanding file history, not assigning fault.

---

## 13. Branching

### 13.1 Definition
A **branch** is a lightweight, movable pointer to a commit.

Branches help isolate development work.

### 13.2 Common Use Cases

| Type                | Purpose                                                        |
|---------------------|----------------------------------------------------------------|
| Maintenance         | Stable bugfix-only version                                     |
| Feature             | Work on specific new features                                  |
| Experimental/Fork   | Alternative implementations or separate project directions     |

### 13.3 Managing Branches

```bash
git branch              # list branches
git branch newbranch    # create a new branch
git checkout newbranch  # switch to a branch
git checkout -b newbranch commit  # create and switch
git branch -d name      # delete a branch (warns if commit is unmerged)
git branch -D name      # force delete
git branch -m old new   # rename branch
```

### 13.4 Visual Representation


```text
            A---B---C (master)
                     \
                      D---E---F (feature)
```

- `master` and `feature` point to different commits.
- Use `git checkout` to switch between them.
- Commits form a Directed Acyclic Graph (DAG), where arrows point backwards to parent commits.

---

## 14. Merging

### 14.1 Purpose
Combines content from two different branches into a single commit.

```bash
git merge branchname
```

### 14.2 Merge Commit
When merging master with another branch, Git auto-generates a new commit containing both histories.

If there's no conflict:
- Git auto-merges changes.
- Creates a new commit with lineage from both parents.

### 14.3 Merge Conflicts
Occurs when the same lines are changed in both branches.

Git inserts markers like:

```text
<<<<<<< HEAD
old version
=======
new version from other branch
>>>>>>> branchname
```

You must manually resolve conflicts and commit the result.

### 14.4 Merge Algorithms

- Git identifies the "closest common ancestor" (e.g., commit A).
- Computes changes from A to B (`diff B A`) and A to C (`diff C A`).
- If non-overlapping, Git applies changes cleanly.
- Overlapping changes cause a conflict requiring manual intervention.

---

## 15. Rebasing

### 15.1 Definition
Rebasing re-applies commits from one branch to another base commit.

```bash
git rebase branchname
```

Instead of creating a merge commit, rebasing rewrites history to make it appear as if your changes were applied on top of the target branch.

### 15.2 Visual Comparison

**Merge:**

```text
    A---B---C---M (merged)
         \     /
          D---E
```

**Rebase:**

```text
    A---B---C---D'---E' (rebased)
         \
          D---E
```

- Rebase creates new commits (`D'`, `E'`) with same changes, but different parent.
- Resulting history is "clean", linear.

### 15.3 When to Use
- Clean, linear history after local development before pushing.
- Avoid publish-rebase: rewriting shared history causes complications.

---

## 16. Best Practices

### 16.1 Commit Messages
- Describe reasoning, not just change.
- Avoid generic messages like “xyz.”

### 16.2 Avoid Perfectionism
- Don't rely heavily on `--amend` early on.
- Mistakes are natural and traceable; history should reflect development flow.

### 16.3 Merging vs. Rebasing
- Merging preserves actual development paths.
- Rebasing simplifies history — useful for polishing before sharing.

---

## Summary

This lecture discussed fundamental Git operations including committing, viewing differences, staging changes, and inspecting history. It elaborated on the three data states in Git (working directory, index/staging area, object database), how differences can be viewed with various `git diff` variations, and how Git uses SHA-1 for commit hashes. It introduced commit metadata importance, branch management (creation, switching, deleting, merging), and explained merging mechanics including conflict resolution. The lecture also explained rebasing as an alternate to merges and emphasized clean history and collaboration conventions. Additional commands such as `git status`, `git blame`, `git grep`, and `git ls-files` were explained for practical usage.