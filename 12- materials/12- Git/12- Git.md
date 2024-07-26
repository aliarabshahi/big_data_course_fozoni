## What is Git

Git is a free and open source distributed **Version Control System (VCS)** designed to handle everything from small to very large projects with speed and efficiency.

### Installing Git

https://git-scm.com/download/win

```bash
$ git init
 
$ git status

$ git add .
# After running "git add .", the changes will be staged, and you can proceed to create a commit using the "git commit" command.

# "staging" refers to the process of preparing changes to be included in the next commit.

$ git commit -m "my first try"

ERROR

$ git log --pretty=format:"%an <%ae>" | sort -u
# see if there were any users on the computer

$ git config --global user.email "fozouni@hotmail.com"
$ git config --global user.name "fozouni"
```

### Now go to Github

1- Make a repository with the same name as your local folder

```bash
$ git remote add origin https://github.com/fozouni/repository.git
```

### Go to .git/config

You should see something like this

```yaml
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/fozouni/repository.git
	fetch = +refs/heads/*:refs/remotes/origin/*
```

### Now

```bash
$ git branch -M main

# will change the branch from master to main

$ git push -u origin main
# The command git push -u origin main is used to push your local Git repository's branch named "main" to the remote repository named "origin." The flag -u is for --set-upstream, is used to set up the tracking relationship between the local branch and the remote branch
```

### Change a file

```bash
$ notepad script.py
or
$ nano script.py

$ git status

$ git add .\script.py

$ git push origin main

$ git log
# or git log --oneline

$ git show <COMMIT NUMBER>
```

### Commit from Github 

Make a change in a file in github and then

```bash
$ git pull 
```

### Create some branches from cli

```bash
$ git branch -a

$ git branch -c de1

$ git checkout de1

# will switch the branch

$ notepad .gitignore
or
$ nano .gitignore

# inside file write for example file.txt which is the home of your passwords

$ git add .

$ git commit -m ".gitignore file has been added"

$ git push -u origin main
```

### Set aliases in Git Bash

```bash
$ cd ~

$ ls -a

$ nano .bashrc

$ alias c='clear'

$ source ~/.bashrc
```

### Rolling back

**This depends on these conditions**

1- Our file has been staged or not?

2- Our file has been committed or not? 

```bash
$ git checkout file.name
#will undo the changes before commiting

$ git diff
# before staging a file it will show us the difference
# git diff --cached

$ git restore --staged jupyter1.ipynb
# will undo files for us if they have gone to staged level

🛑 If we have commited a file we should do this

$ git log --oneline

$ git diff ace00c4..7dfdf5c

$ git reset --hard ec62a6f
# every commit after "ec62a6f" will be removed 

$ git revert ec62a6f
# will revert ec62a6f commit
```

### SSH

```bash
cat .git/config

$ ssh-keygen.exe

Now put the public key in your github setting part
```

### Some notes

**windows versus Linux**

```bash
$ New-Item script.py
$ touch script.py
```

### Install GitHub CLI

Go to [**this address**](https://cli.github.com/) and easily install GitHub CLI. Then clone one of your repo like this (note that the cli will ask you to provide some info first)

```bash
$ gh repo clone fozouni/st-app
```

