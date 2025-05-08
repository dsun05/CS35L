# Shell Commands
---


---

## cd — Change the current directory

### SYNOPSIS

```
cd [DIRECTORY]
```

#### DESCRIPTION

The cd (change directory) command changes the current working directory to the specified DIRECTORY. This affects the current shell session and any relative file paths used afterward.

If no DIRECTORY is provided, cd changes to the user’s home directory.

#### COMMON USAGE
	•	cd ~ or cd: Go to the home directory
	•	cd -: Switch to the previous directory
	•	cd ..: Move one directory up (to the parent directory)
	•	cd /: Go to the root directory

#### EXAMPLES

1.	Go to your home directory

```
cd
```

2.	Navigate into a subdirectory

```
cd projects/myapp
```

3.	Return to the previous directory

```
cd -
```

4.	Move up two directory levels

```
cd ../..
```

5.	Go to the root of the file system

```
cd /
```

---

---

## ls — List directory contents

### SYNOPSIS

```
ls [OPTIONS] [FILE...]
```

#### DESCRIPTION

The ls command lists files and directories in the current or specified directory.

#### OPTIONS
	•	-l, --long: Use a long listing format to display detailed information.
	•	-a, --all: List all entries, including hidden files (those starting with a dot).
	•	-h, --human-readable: Show file sizes in human-readable format (e.g., 1K, 234M).
	•	-R, --recursive: List directories and their contents recursively.

EXAMPLES
1.	List all files including hidden:

```
ls -a
```

2.	Long listing with human-readable sizes:

```
ls -lh
```
---

---

## pwd — Print working directory

### SYNOPSIS

```
pwd
```

#### DESCRIPTION

The pwd command outputs the absolute path of the current working directory.

#### EXAMPLES
1.	Display the current working directory:

```
pwd
```

---

---

## mkdir — Make directories

### SYNOPSIS

```
mkdir [OPTION] DIRECTORY...
```

#### DESCRIPTION

The mkdir command creates directories with the specified name(s).

#### OPTIONS
	•	-p, --parents: Create parent directories as needed.
	•	-v, --verbose: Print a message for each directory created.

#### EXAMPLES
1.	Create a directory:

```
mkdir new_folder
```

2.	Create nested directories:

```
mkdir -p parent/child/grandchild
```

---

---

## cp — Copy files and directories

### SYNOPSIS

```
cp [OPTIONS] SOURCE DEST
```

#### DESCRIPTION

The cp command copies files or directories from SOURCE to DEST.

#### OPTIONS
	•	-r, --recursive: Copy directories recursively.
	•	-p, --preserve: Preserve file attributes (timestamps, permissions).
	•	-i, --interactive: Prompt before overwriting files.

#### EXAMPLES
1.	Copy a file:

```
cp file1.txt file2.txt
```

2.	Recursively copy a directory:

```
cp -r dir1/ dir2/
```

---

---

## mv — Move or rename files

### SYNOPSIS

```
mv [OPTION] SOURCE DEST
```

#### DESCRIPTION

The mv command is used to move or rename files and directories.

#### OPTIONS
	•	-i, --interactive: Prompt before overwriting files.
	•	-u, --update: Move only when the source file is newer than the destination file or when the destination file is missing.
	•	-v, --verbose: Print a message for every file moved.

#### EXAMPLES
1.	Rename a file:

```
mv oldname.txt newname.txt
```

2.	Move a file to another directory:

```
mv file.txt /path/to/destination/
```

---

---

## rm — Remove files or directories

### SYNOPSIS

```
rm [OPTION] FILE...
```

#### DESCRIPTION

The rm command removes files or directories from the filesystem. It is a destructive operation and should be used with caution.

#### OPTIONS
	•	-f, --force: Force removal of non-existent files without prompting.
	•	-r, --recursive: Remove directories and their contents recursively.
	•	-i, --interactive: Prompt before every removal.
	•	-v, --verbose: Print a message for every file removed.

#### EXAMPLES
1.	Remove a file:

```
rm file.txt
```

2.	Force delete without prompt:

```
rm -f file.txt
```

3.	Recursively delete a directory:

```
rm -r mydir/
```

---

---

## cat — Concatenate and display file content

#### SYNOPSIS

```
cat [OPTIONS] [FILE...]
```

#### DESCRIPTION

The cat command concatenates and displays the content of files.

#### OPTIONS
	•	-n, --number: Number all output lines.
	•	-b, --number-nonblank: Number non-empty output lines.

#### EXAMPLES
1.	Display a file:

```
cat file.txt
```

2.	Concatenate multiple files:

```
cat file1.txt file2.txt > combined.txt
```

---

---

## echo — Display a line of text

#### SYNOPSIS

```
echo [OPTION] STRING...
```

#### DESCRIPTION

The echo command outputs the specified text or variables to the standard output.

#### OPTIONS
	•	-n: Do not output the trailing newline.
	•	-e: Enable interpretation of backslash escapes (e.g., \n for new line).
	•	-E: Disable interpretation of backslash escapes.

#### EXAMPLES

1.	Print a message:

```
    echo "Hello, World!"
```

2.	Print without newline:

```
echo -n "Hello"
```

---

---

## grep — Pattern search in files

### SYNOPSIS

```
grep [OPTIONS] PATTERN [FILE...]
```

#### DESCRIPTION

The grep command searches for lines in a file that match a specified pattern. It supports regular expressions and various options for case sensitivity, line numbering, etc.

#### OPTIONS
	•	-i, --ignore-case: Ignore case distinctions.
	•	-r, --recursive: Recursively search directories.
	•	-v, --invert-match: Invert the match (show lines that do not match the pattern).
	•	-n, --line-number: Show line numbers in the output.
	•	-l, --files-with-matches: Print only the names of files with matching lines.
	•	-c, --count: Print only the count of matching lines.

#### EXAMPLES
1.	Case-insensitive search:

```
grep -i "error" logfile.txt
```

2.	Recursive search for “TODO”:

```
grep -r "TODO" .
```

3.	Show line numbers:

```
grep -n "404" access.log
```

---

---

## find — Search for files in a directory hierarchy

### SYNOPSIS

```
find [PATH...] [EXPRESSION]
```

#### DESCRIPTION

The find command searches for files and directories recursively, based on various criteria such as name, size, time, etc.

#### OPTIONS
	•	-name PATTERN: Search for files matching the pattern.
	•	-mtime N: Find files modified N days ago.
	•	-size +N: Find files larger than N bytes.
	•	-exec COMMAND {} \;: Execute a command on each matched file.

#### EXAMPLES
1.	Find files by name:

```
find . -name "*.txt"
```

2.	Find files modified in the last 7 days:

```
find . -mtime -7
```

3.	Delete .tmp files:

```
find . -name "*.tmp" -delete
```

---

---

## chmod — Change file permissions

### SYNOPSIS

```
chmod [OPTION] MODE FILE
```

#### DESCRIPTION

The chmod command changes the permissions of a file or directory. It can set permissions in either symbolic or octal format.

#### OPTIONS
	•	-R, --recursive: Apply changes recursively to directories.
	•	-v, --verbose: Output a diagnostic for every file processed.
	•	-c, --changes: Output only when a file is actually changed.
	•	-f, --silent: Suppress most error messages.

#### EXAMPLES
1.	Grant execute permission to the user:

```
chmod u+x script.sh
```

2.	Remove write permission from group:

```
chmod g-w file.txt
```

3.	Set full permissions (read, write, execute) for all users:

```
chmod 777 file.txt
```

4.	Recursively change permissions for directories:

```
chmod -R 755 dir/
```

---

---

## ps — Show running processes

### SYNOPSIS

```
ps [OPTION]
```

#### DESCRIPTION

The ps command displays information about running processes on the system.

#### OPTIONS
	•	-a: Show processes for all users.
	•	-x: Show processes not attached to a terminal.
	•	-e, --everyone: Display all processes.
	•	-f: Show full format (includes command with arguments).
	•	-u USER: Show processes for a specific user.

#### EXAMPLES
1.	Show all processes:

```
ps -e
```

2.	Show processes with detailed information:

```
ps -ef
```

---

---

## tr — Translate or delete characters

### SYNOPSIS

```
tr [OPTION] SET1 [SET2]
```

### DESCRIPTION

The tr command is used to translate, replace, or delete characters in a stream of text. It works by reading from the standard input and performing the transformations specified.

### OPTIONS
	•	-d, --delete: Delete characters in SET1.
	•	-s, --squeeze-repeats: Replace each sequence of a repeated character in SET1 with a single occurrence.
	•	-c, --complement: Use the complement of SET1, i.e., all characters except those in SET1.
	•	-t, --truncate-set1: Truncate SET1 to SET2 length.

### EXAMPLES
1.	Convert lowercase to uppercase:

```
echo "hello" | tr 'a-z' 'A-Z'
#### Output: HELLO
```

2.	Delete digits:

```
echo "hello 123" | tr -d '0-9'
#### Output: hello 
```

3.	Squeeze repeated spaces:

```
echo "this    is    a test" | tr -s ' '
#### Output: this is a test
```

---

---

## awk — Pattern scanning and processing language

### SYNOPSIS

```
awk 'pattern { action }' [FILE...]
```

#### DESCRIPTION

awk is a powerful programming language used for pattern scanning and processing. It is commonly used for extracting and manipulating text data.

#### OPTIONS
	•	-F, --field-separator=SEP: Set the field separator to SEP (default is whitespace).
	•	-v, --assign=var=value: Assign a value to a variable before starting the program.
	•	-f, --file=program-file: Read the awk program from the given file.

#### EXAMPLES
1.	Print the second column of a file:

```
awk '{print $2}' file.txt
```

2.	Sum the values in the first column:

```
awk '{sum += $1} END {print sum}' numbers.txt
```

3.	Use a custom field separator (comma-separated values):

```
awk -F ',' '{print $1, $2}' file.csv
```

---

---

## sort — Sort lines of text

### SYNOPSIS

```
sort [OPTIONS] [FILE...]
```

#### DESCRIPTION

The sort command arranges lines in text files in a specified order. Sorting can be done alphabetically, numerically, or by other criteria.

#### OPTIONS
	•	-r, --reverse: Reverse the result of comparisons.
	•	-n, --numeric-sort: Sort by numerical value instead of lexicographical.
	•	-k, --key=KEY: Sort by the given key (field).
	•	-u, --unique: Output only the first occurrence of duplicate lines.
	•	-f, --ignore-case: Ignore case when sorting.

#### EXAMPLES
1.	Sort alphabetically:

```
sort names.txt
```

2.	Sort by numerical value:

```
sort -n scores.txt
```

3.	Sort by the second column:

```
sort -k2 file.txt
```

---

---

## uniq — Report or filter repeated lines

### SYNOPSIS

```
uniq [OPTION] [INPUT [OUTPUT]]
```

#### DESCRIPTION

The uniq command is used to filter out repeated lines from a file or input. It can also count the occurrences of lines or display only duplicate lines.

#### OPTIONS
	•	-c, --count: Prefix lines with the number of occurrences.
	•	-d, --repeated: Only print duplicate lines.
	•	-u, --unique: Only print lines that are unique.
	•	-i, --ignore-case: Ignore case differences when comparing lines.

#### EXAMPLES
1.	Remove duplicate lines (input must be sorted):

```
sort data.txt | uniq
```

2.	Count occurrences of lines:

```
sort data.txt | uniq -c
```

3.	Show only repeated lines:

```
sort data.txt | uniq -d
```

---

---

## rmdir — Remove empty directories

### SYNOPSIS

```
rmdir [OPTION] DIRECTORY...
```

#### DESCRIPTION

The rmdir command removes empty directories. It does not remove directories that contain files or other directories.

#### OPTIONS
	•	-p, --parents: Remove parent directories as well if they become empty after the operation.
	•	-v, --verbose: Print a message for each directory removed.

#### EXAMPLES
1.	Remove a single empty directory:

```
rmdir emptydir
```

2.	Remove multiple empty directories:

```
rmdir dir1 dir2
```

3.	Remove a directory and its parent if empty:

```
rmdir -p parent/child
```

---

---

## comm — Compare two sorted files line by line

### SYNOPSIS

```
comm [OPTION] FILE1 FILE2
```

#### DESCRIPTION

The comm command compares two sorted files line by line, outputting three columns:
	1.	Lines unique to FILE1
	2.	Lines unique to FILE2
	3.	Lines common to both files.

#### OPTIONS
	•	-1: Suppress column 1 (lines unique to FILE1).
	•	-2: Suppress column 2 (lines unique to FILE2).
	•	-3: Suppress column 3 (common lines).

#### EXAMPLES
1.	Compare two files and show common lines:

```
comm -12 file1.txt file2.txt
```

2.	Suppress lines unique to file1.txt:

```
comm -1 file1.txt file2.txt
```

---

---

## eval — Evaluate arguments as a shell command

### SYNOPSIS

```
eval [COMMAND_STRING]
```

#### DESCRIPTION

The eval command takes a string as an argument and evaluates it as a shell command. It is typically used when you need to construct commands dynamically.

#### OPTIONS
	•	No specific options. The only argument is the command string that is to be executed.

#### EXAMPLES
1.	Evaluate a dynamic command:

```
cmd="ls -l"
eval $cmd
```

2.	Use variables in dynamic commands:

```
dir="home/user"
eval "cd $dir && ls"
```

---

---

## kill — Send signals to processes

### SYNOPSIS

```
kill [OPTION] PID...
```

#### DESCRIPTION

The kill command sends a signal to a process, usually to terminate it.

#### OPTIONS
	•	-9, --kill: Force the process to terminate immediately.
	•	-l, --list: List all available signals.
	•	-15, --terminate: The default signal, which requests a graceful termination.

#### EXAMPLES
1.	Kill a process by PID:

```
kill 1234
```

2.	Force kill a process:

```
kill -9 1234
```

3.	Kill all processes by name:

```
killall firefox
```

---