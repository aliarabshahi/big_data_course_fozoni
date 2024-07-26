### Step 1: Get tweets regularly

```bash
$  mkdir -p /home/amin/data/stage/step1 /home/amin/data/stage/step2 

$ cd /home/amin/data

$ mkdir lake logs

$ mkdir -p /home/amin/data/scripts

#You need some editor like nano

sudo apt-get update

sudo apt install nano

$ crontab -l
no crontab for amin

$ sudo usermod -a -G crontab $(whoami)
[sudo] password for amin:

$ sudo service cron restart
$ crontab -e

$ watch -n 5 ls -lh .
# -n specifies the interval in seconds between executions

###################################################################
To see how we can set cronjobs, see the following blog post:

https://crontogo.com/blog/the-complete-guide-to-cron/
###################################################################

$ cd /home/amin/data/scripts

$ nano get_tweets.sh

# Note that in the following line, "#!" sign is called a shebang.  It is used to tell the operating system which interpreter to use to execute the script.

$ which bash

#!/usr/bin/bash
/usr/bin/curl -s -H "User-Agent:Chrome/123.0" https://www.sahamyab.com/guest/twiter/list?v=0.1 | /usr/bin/jq '.items[0,2,3,4,5,6,7,8,9,10] | [.id, .sendTime, .sendTimePersian, .senderName, .senderUsername, .type, .content] | join(",") ' > /home/amin/data/stage/step1/$(date +%s).csv

$ chmod +x  ./get_tweets.sh
$ crontab -e 

* * * * * /home/amin/data/scripts/get_tweets.sh

$ watch -n 5 ls -lh ~/data/stage/step1
```



###  Step 2: Combine CSV files

```bash
$ cd /home/amin/data/scripts
$ nano  combine_csv.sh

#!/usr/bin/bash
sleep 20;

flist=$(ls /home/amin/data/stage/step1)

stage1="/home/amin/data/stage/step1"
stage2="/home/amin/data/stage/step2"

fname="$stage2/$(date +%Y-%m-%d-%H).csv"

logfile=/home/amin/data/logs/step2.log

echo "Begin at $(date)" >> $logfile
for i in $flist ; do
        echo $i >> $logfile;
        current="$stage1/$i";
        echo "concatenating $current into $fname " >> $logfile ;
        sed -i "s/\"//g" $current;
        cat $current >> $fname;
        echo "deleting $current ..." >> $logfile;
        rm $current;
done;
echo "Sucessful" >> $logfile

###################################################################
# Note that the command " sed -i "s/\"//g" $current" removes " sign globally from $current.

# If you want to know more regarding SED, read the following blog post
# https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/
###################################################################

$ chmod +x ./combine_csv.sh


$ crontab -e

* * * * * /home/amin/data/scripts/combine_csv.sh


$ tail -f /home/amin/data/logs/step2.log
```

### Step 3: Convert CSV files to Parquet format by python

```bash
$ sudo apt install python3 python3-pip virtualenv launchpadlib

$ pip3 install pandas pyarrow

###################################################################
# Pyarrow: This library provides a Python API for functionality provided by the Arrow C++ libraries, along with tools for Arrow integration and interoperability with pandas, NumPy, and other software in the Python ecosystem.
###################################################################


$ cd /home/amin/data/scripts
$ nano convert_to_parquet.py

#!/usr/bin/python3
import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], header=None , names=['id','sendTime','sendTimePersian', 'senderName', 'senderUsername', 'type', 'content' ],dtype={'content': object})

df.to_parquet( f"{sys.argv[2]}/{sys.argv[1].split('/')[-1].split('.')[0]}.parquet")

$ python3 convert_to_parquet.py /home/amin/data/stage/step2/2023-06-05-20.csv /home/amin/data/lake/

###################################################################
# To run the above command, you should copy "convert_to_parquet.py" file to the directory
# /home/amin/data/stage/step2/2023-06-05-20.csv 

###################################################################
# What is sys.argv?
# In the following command
$ python sample.py Hello Python

# Then inside sample.py, arguments are stored as: 

# sys.argv[0] == ‘sample.py’ 
# sys.argv[1] == ‘Hello’ 
# sys.argv[2] == ‘Python’
###################################################################
```

### Step 4: Final step

```bash
$ nano /home/amin/data/scripts/convert_to_parquet.sh

#!/usr/bin/bash
stage2="/home/amin/data/stage/step2"
flist=$(ls $stage2)
lake=/home/amin/data/lake
logfile=/home/amin/data/logs/step3.log

echo "Begin at $(date)" >> $logfile
for i in $flist ; do
        echo $i >> $logfile;
        current="$stage2/$i";
        echo "converting $current to parquet " >> $logfile ;
        /usr/bin/python3 /home/amin/data/scripts/convert_to_parquet.py $current $lake ;   
        echo "deleting $current ..." >> $logfile;
done;
echo "Sucessful" >> $logfile

$ chmod +x ./convert_to_parquet.sh

$ crontab -e

*/2 * * * * /home/amin/data/scripts/convert_to_parquet.sh
```

### See your results in CLI

```bash
$ pip3 install parquet-cli
$ parq input.parquet --head 10
```

**Congratulation to you! 🤗**

------

## Appendix

### More explanation regarding `sys.argv`

What exactly  **`{sys.argv[2]}/{sys.argv[1].split('/')[-1].split('.')[0]}`** does?

```Text
This is a Python command line argument syntax. It's taking two command line arguments and performing some string manipulations and file path joining.

Breaking it down:

sys.argv is a list of command line arguments passed to the Python script.

- sys.argv[1] is the first command line argument 
- sys.argv[2] is the second command line argument

The code is doing:

1) sys.argv[1].split('/')[-1].split('.')[0]

This splits the first argument by '/' (file path separator) and takes the last part (-1), then splits that by '.' and takes the first part (before the first '.'). This extracts just the file name without extension.

2) {sys.argv[2]}

This is a string format, placing the second command line argument inside the {} brackets.

3) Combining 1) and 2) - it's joining the directory from the second argument with the filename from the first argument.

So if you ran:

`python script.py folder/file.txt directory`  

sys.argv would be:

[ 'script.py', 'folder/file.txt', 'directory']

Then the result of the code would be: 

`directory/file`

Joining the directory ("directory") with just the filename ("file") part from the full file path ("folder/file.txt").

So in summary, this code is taking a file path as the first argument and a destination directory as the second argument, and generating the full path to that file in the destination directory.

Hope this explanation helps! Let me know if you have any other questions.
```

