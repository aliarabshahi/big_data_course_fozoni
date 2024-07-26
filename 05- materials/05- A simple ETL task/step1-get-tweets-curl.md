### Follow these instructions:

```bash
$ curl https://www.sahamyab.com/guest/twiter/list?v=0.1
```

```bash
$ curl -H "User-Agent:Chrome/123.0" https://www.sahamyab.com/guest/twiter/list?v=0.1
```

### Install jq library (json query):

```bash
# In Linux, before installing any program by apt, you should update apt as follows
$ sudo apt-get update

$ sudo apt install jq
```

### Now you can see it better:

```bash
$ curl -H "User-Agent:Chrome/123.0" https://www.sahamyab.com/guest/twiter/list?v=0.1 | jq

$ curl -s -H "User-Agent:Chrome/123.0" https://www.sahamyab.com/guest/twiter/list?v=0.1 | jq '.items'

# to see the tenth item use the following command
$ curl -s -H "User-Agent:Chrome/123.0" https://www.sahamyab.com/guest/twiter/list?v=0.1 | jq '.items[10]'

$ curl -H "User-Agent:Chrome/123.0" https://www.sahamyab.com/guest/twiter/list?v=0.1| jq '.hasMore, .success, .items[].id'

$ curl -s -H "User-Agent:Chrome/123.0" https://www.sahamyab.com/guest/twiter/list?v=0.1 | jq '.items[] | [.id, .sendTime, .sendTimePersian, .senderName, .senderUsername, .type, .content] | join(",") ' 
```

### We can read from .json files:

```bash
$ cat .\wt.json | jq '.actions[].command' >> test.json

$ cat .\wt.json | jq '.actions[].command' >> C:\Users\Golestan\Desktop\test.json
```

🛑**Work on the outputs of Telegram Channels**🛑

### Some notes:

```bash
$ date +%s

# If date +%s = 1689745809 you can see the exact time by the following command! 
$  date --date='@1689745809'

#instead of "amin' you should write your own username!
$ chmod 764 /home/amin

$ mkdir stage

$ ls -lh stage
```

### Create an output:

```bash
$ curl -s -H "User-Agent:Chrome/123.0" https://www.sahamyab.com/guest/twiter/list?v=0.1 | jq '.items[] | [.id, .sendTime, .sendTimePersian, .senderName, .senderUsername, .type, .content] | join(",") ' > stage/$(date +%s).csv

$ ls -lh stage
```

