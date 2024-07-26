# `Linux Operating System`

### `Common Operating Systems (OS)`

We have three main OS; **Windows, Linux** and **Mac.** 

- Windows is suitable for daily jobs.
- Linux and Mac are more focused on Programming and other professional stuffs.  

------

### `Why Linux?`

• Open Source Operating System (OS)
• Eagerly chosen by programmers. Why?
	– It’s free
	– More secure, it will protect your systems from trojans, viruses, adware etc.
	– Easy to customize
	– Variety of distribution: Ubuntu, Fedora, Deepin and many more…
• Linux is heavily documented
• Over 1000 commands, but I will present you some of the most common ones in daily basis.

------

### `An Important Note`

• In linux and all unix-based OS (like Mac) we have `/`  (**forward slash**) in our file system. But in Windows OS we have `\` (**back slash**).

- D:\others\st-app
- /home/amin/spark

------

### `Some useful cli commands for interacting with wsl`

```bash
wsl -l -v
# will list all wsl distros for us

wsl --set-version Ubuntu-20.04 2
# set the version of our wsl to 2

wsl -l --online
#show us a list of available distros

wsl --install -d Debian
#install for us the Debian distro
```

------

## Some Linux commands!

### `1- cd DIRECTORY`

• Change directory from your current position
• Probably the most common command in linux
• You can pass DIRECTORY as relative or absolute path
– cd ~/absolute/path/to/Directory
– cd relative/path/to/Directory
– cd Directory
• cd ~ move to home directory (the same behaviour as cd alone)
• cd ../ move one directory up, can be used multiple time, for example cd ../../../
• cd- move to previously used directory

------

### `2- cat [ O P T I O N ] … FILE/S …`

• Display content of file/s on the standard output
• Possible to display a content of one, multiple file and to concatenate content of
different files together using `>` and `>>` operators
• Examples:
– cat file.txt : display content of file.txt in the terminal
– cat file1.txt file2.txt : display content of both, first file1.txt and second file2.txt
– cat file1.txt file2.txt > combined_files.txt : concatenate two files and save it
as a new file called combined_files.txt with `>` operator, which is used for output redirection
– cat additional.txt >> existing.txt : add additional.txt content at the end of existing.txt file, `>>` operator is used for appending output.



------

### `3- echo LONG - OPTION`

• Display text or variables as output, it is commonly used in shell scripts
• It is often used in shell scripting to display messages, debug scripts, or generate dynamic
output
• Examples:
– echo "Hello, world!” : print “Hello, world” in the terminal
– name="John”
echo "My name is $name” : print “My name is John” in the terminal
– echo "This is a new line.\nThis is a tab:\t\tAnd this is a backslash: \\”
• The use of escape sequences such as \n and \t with the echo command is necessary to format
and control the output by inserting new lines, tabs, and other special characters for improved
readability and presentation.

------

### `4- man COMMAND`

• man is an interface to the on-line reference manuals, it is used to display the manual
pages (documentation) for various commands, programs, and system functions
• It provides detailed information about command usage, options, syntax, and examples
• For example:
– man find : display manual page for the `find` command
• Using the man command is a great way to explore and learn about various commands,
functions, and system features available in Linux, providing you with detailed
documentation to understand their usage and options thoroughly.

------

### `5- ls [OPTION] … DIRECTORY / IES`

• List files and directories on current or given directory
• The second most known command J
• useful flags:
– ls –a list all files including hidden files.
– ls -l list with long format.
– ls –R recursively list subdirectories.
• ls path/to/Directory list files in given path.
• ls path/to/Directory1 path/to/Directory2 list files in given directories.

------

### `6- pwd (comes from Present Working Directory)`

• find the path to current working directory
• useful inside scripts to specify absolute path
• for example:
– pwd print current location
– echo "Your current location is: $(pwd)” to print current location
– location=$($pwd) to store path to current location

------

### `7- mkdir [OPTION] … DIRECTORY / IES …`

• Make directories much faster than with manual clicking
• If you want to create multiple directories at once, just separate their names with space
• Useful flags:
 -v : prints a message for each created directory

 -p : create intermediate directories as required, without this flag all intermediate directories need to
exist already
• For example:
– mkdir new_directory creates a directory called “new_directory”.
– mkdir –p new/intermediate/dirs will create 3 new directories if none of them already exist.

------

### `8- cp [OPTION ] … SOURCE … DESTINATION`

• Copy files or directories with their content wherever you want
• Useful flags:
– -v : cause cp to be verbose, showing files as they are copied.
– -r (or –R) : copy directory content recursively
• For example:
– cp file.txt /home/files – copy file.txt and paste it to /home/files directory
– cp file1.txt file2.txt file3.txt /home/files - copy file1,2,3 to /home/files/ directory
– cp file1.txt file2.txt copy file1.txt and create a copy file2.txt in the same directory
– cp –R /home/files/photos /home/files/destination copy photos directory to destination dir

------

### `9- mv [OPTION] … SOURCE … DESTINATION`

• Rename or move files and directories with their content from one destination to another
• Useful flags:
– -i : interactive mode, which prompts for confirmation before overwriting existing files
• Examples:
– mv file.txt renamed_file.txt rename file.txt to renamed_file.txt
– mv file.txt /home/files/ move file.txt to files directory
– mv file1.txt file2.txt /home/files/ move multiple files simultaneously

------

### `10- rm [OPTION] … FILE/S …`

• Remove file, files or directories with their content depending on syntax being used
• Useful flags:
– -i : interactive mode, asking for confirmation before deleting a file
– -r : enable you to remove directories with their content
– -v : be verbose when deleting files, showing them as they are removed.
• Remember to use the rm command with caution as it permanently deletes files and
directories.
• Double-check your commands before executing them to avoid accidental data loss.

------

### `11- touch [OPTION] … FILE/S …`

• Create an empty file or generate and modify a timestamp
• For example:
– touch file.txt create a new fille called file.txt in the current directory, if the file exists command
updates the file’s timestamp to the current time without modyfing its content
• Using the touch command can be helpful when you need to ensure that a file exists or
when you want to update the timestamps of files for various purposes, such as sorting
files based on their modification times or triggering certain actions based on file
access times.

------

### `12- find [OPTION] [PATH] [EXPRESSION]`

• Search for files and directories in a directory hierarchy based on specified criteria and
perform subsequent operations if given
• For example:
– find . –type f : it finds all files in the current directory ( `.` - current directory)
– find /path/to/search -type d -name "directory_name” – finds all directories with name
“directory_name” in the ”path/to/search” directory
– find /path/to/search -name "*.txt" -exec cat {} \; search for files in the /path/to/search directory that
have a .txt extension and displays the content of those files in the terminal
• The find command is very versatile and allows for complex searches based on various
criteria. By combining different options and operators, you can create sophisticated file
searches.

------

### `13- tar [OPTIONS] … FILE`

• Create, manipulate and extract files from tape archives (tar files) with optional
compression.
• Useful flags:
 -c : create an archive file
 -x : extract the archive file
 -f : specify the name of the archive file
 -v : displays verbose information
 -z : compress the resulting archive with gzip.

• Create a tar archive from few files:
– tar -cvf archive.tar file1.txt file2.txt
• Extract files from a tar archive:
– tar -xvf archive.tar
• Extract files from a tar archive to a specific directory:
– tar -xvf archive.tar -C /path/to/destination
• Compress files while creating a tar archive:
– tar -czvf archive.tar.gz directory.

------

### `14- grep [OPTIONS ] … PATTERN FILE/S …`

• One of the most useful commands, especially while dealing with a lot of text data, for example log files.
• Print lines matching a pattern, it lets you find a pattern by searching through all the texts in a specific file.
• Useful flags:
-i: matches patterns case-insensitively
-v: prints lines which do not match the given pattern
-r: recursively search in sub/directories
-l: prints only the names of the files containing the pattern
-c: prints only the count of matching lines
-E: extended regular expressions
-o: outputs only the matched portion of the line
-n: display line numbers
• The tool is highly versatile and can be combined with regular expressions to perform more advanced text
searching and manipulation tasks!

• grep is a powerful command-line tool used for searching and filtering text.
• It is commonly used for log searching, allowing developers to quickly pinpoint errors
or extract relevant information from log files.
• It's also useful for searching through files in a directory, enabling programmers to
locate specific code snippets or configurations.
• grep can be applied in natural language processing (NLP) tasks, such as extracting
specific patterns or analyzing textual data.
• With its flexibility and power, grep proves to be an essential tool for programmers in
daily tasks involving text analysis and retrieval

------

### `15- head [OPTION] … FILE/S`

• Display the beginning lines of a file or input, it is commonly used to preview the content of files
• It is often used to quickly examine the first few lines of a file without opening the entire file
• Examples:
– head file.txt : display the first 10 lines of the file.txt in the terminal
– head -n 5 file.txt : display the first 5 lines of the file.txt in the terminal
– head -c 20 file.txt : display the first 20 bytes of the file.txt in the terminal
• -The use of options such as -n and -c with the head command allows customization of the
number of lines or bytes to be displayed, providing flexibility in previewing file content as
needed.

------

### `16- tail [OPTION] … FILE/S`

• Display the ending lines of a file or input, commonly used to view the last few lines of files
• It is often used to monitor log files or display the most recent entries in a file
• Examples:
– tail file.txt : display the last 10 lines of the file.txt in the terminal
– tail -n 5 file.txt : display the last 5 lines of the file.txt in the terminal
– tail -f file.txt : continuously display the last lines of the file.txt as it updates (useful for monitoring log
files)
• The use of options such as -n and -f with the tail command allows customization of the
number of lines to be displayed or to follow the updates of a file in real-time.

------

### `17- history`

• List up to 1000 of previously executed commands (we can change it)
• It is often used to recall and rerun previous commands, saving time and improving
productivity
• Examples:
– history : display a numbered list of previously executed commands in the terminal
– history -c : clear the command history
• The history command provides a convenient way to review past commands,
empowering users to recall and rerun previous actions effortlessly, fostering a
streamlined and efficient command-line workflow.

------

### `18- chmod [OPTIONS] … MODE … FILE/S…`

• It enable modifying a file or directory’s read, write, and execute permissions. Often used in
shell scripting or command-line operations to set permissions on files or directories.

Every actions has an special number as follows:

- read = 4

- write = 2

- execute = 1

• Examples:
– chmod +x script.sh : Add executable permission to the script.sh file
– chmod 644 file.txt : Set read and write permissions for the owner, and read-only permissions for
others on the file.txt
– chmod -R 777 directory : Recursively set full permissions (read, write, execute) for all users on the
directory and its contents
• The use of numeric or symbolic notation with the chmod command allows precise control
over permissions, granting or restricting access for users, groups, and others.

• chmod assigns permissions using three numbers: the first number represents permissions
for the **owner**, the second number for the **group**, and the third number for **others** (<OWNER><USER GROUP><OTHERS>): 

- chmod u=rwx, g=rw, o=r /home/amin
- chmod 764 /home/amin

------

### `19- wget [OPTIONS] … URL …`

• The non-interactive network downloader, it retrieves files using HTTP, HTTPS,
and FTP protocols. Often used to download files, web pages, or entire websites from
remote servers.
• Examples:
– wget https://example.com/file.txt : Download the file.txt from the specified URL
– wget -r -np https://example.com : Download the entire website from the specified URL, recursively
but without following links to external sites
– wget -O output.txt https://example.com/file.txt : Download the file.txt from the specified URL and
save it as output.txt

------

### `20- sudo [COMMAND]`

• Used as a prefix for some commands that only superusers are allowed to run. Often used in
command-line operations to run commands that require elevated permissions.
• Examples:
– sudo apt update : Run the 'apt update' command with administrative privileges to update package
information.
– sudo rm -rf /path/to/directory : Delete a directory and its contents with administrative permissions.
– sudo useradd newuser : Create a new user account with administrative privileges.
• The use of the `sudo` command allows authorized users to perform tasks that require
elevated permissions, providing an additional layer of security and control - use it carefully!

------

### `21- alias [OPTIONS] [NAME] = ‘[VALUE]'`

• This command allows you to create custom shortcuts or abbreviations (aliases) for frequently used
commands or command sequences. It helps to simplify command-line usage by reducing the need
for typing long or complex commands repeatedly.
• Key features of alias:
Aliases are created using the alias command followed by the desired alias name and the command it represents.
Aliases are stored in the user's shell environment and persist across sessions.
Aliases can be customized and tailored to individual preferences or workflow.
• To ensure that aliases are available for use in your terminal indefinitely, you can add them to your
shell's configuration file. The specific file to modify depends on the shell you're using:
For Bash shell: Add aliases to ~/.bashrc or ~/.bash_aliases.
For Zsh shell: Add aliases to ~/.zshrc or ~/.zsh_aliases.

------

### `22- passwd [OPTIONS] … [user name]`

• The passwd command is used to change or update user passwords in Linux systems. It
allows users to manage their own passwords or enables system administrators to modify
user passwords.
• Examples:
– passwd: Change the password for the current user.
– passwd username: Change the password for the specified user (requires administrative privileges).
– passwd -l username: Lock the specified user account by disabling the password.
– passwd -u username: Unlock the specified user account by enabling the password.
– passwd -e username: Force the specified user to change their password during the next login.
– passwd -d username: Remove the password for the specified user, making it passwordless.
– passwd -S username: Display password-related information for the specified user.

------

### `23- ssh user_name@host(IP/domain_name)`

• The ssh command (Secure Shell) is used to establish secure, encrypted remote connections to Linux
servers or devices. It provides a secure method for logging into and executing commands on remote
machines.
• Examples:

​	- ssh username@hostname: Connect to the remote host specified by hostname using the username.

​	- ssh -p port username@hostname: Connect to the remote host using a non-default SSH port

​	- ssh -i private_key_file username@hostname: Connect using a specific private key file instead of the default key

In a programmer's life, the ssh command is commonly used to securely connect to remote servers,
deploy applications, access version control systems (e.g., Git), and execute commands on remote
machines for development, debugging, and system administration purposes.

------

### `EVERYDAY IN WORKING LIFE`

• To navigate through system I need to **change [cd] directories** all the time.
• I need to know what can I find so I need to **list [ls] files** and directories.
• To pack and unpack tarball files I am using **[tar –xzvf / -czvf]** frequently.
• I am looking for a specific file in the system, so I need to **[find]** it.
• Sometimes I am looking for files containing specific phrase so I need to **[find] and [grep]** for it.
• I want to check what command I was using recently so I am looking into **[history]**.
• To login to external server **[ssh]** is my guy.

------

### `Some useful links`

1. Go to https://www.m-fozouni.ir/alias-in-windows-and-linux/ if you want to see how we can set aliases permanently in Windows.
2. You can browse this page https://www.m-fozouni.ir/blog/ for which I regularly write about different things in the world of DE and DS.