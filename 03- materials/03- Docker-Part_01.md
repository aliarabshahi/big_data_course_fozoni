### 1- JSON (JavaScript Object Notation) files and chmod command

```bash
amin@DESKTOP-3F1FI9I:~$ chmod 765 /home/amin/
```

```json
{
    "name": "John Doe",
    "age": 30,
    "isStudent": false,
    "languages": ["JavaScript", "Python", "Java"],
    "address": {
      "street": "123 Main Street",
      "city": "Anytown",
      "country": "USA"
    }
  }

🛑 Recomendation: Install the `JSON Crack` vscode extension
```

### 2- Set up the registry mirror of Docker 

In the `setting > docker engine` path set the following item:

```json
{
  "registry-mirrors": [
    "https://docker.iranserver.com"
  ]
}
```

Docker will first check if the image is available on `https://docker.iranserver.com`. If the image is found there, it will be downloaded from that mirror instead of the default Docker Hub. This is a good job for Iranian citizens which are banned!

### 3- Commands

```bash
$ docker version

$ docker login

$ docker ps --all

$ docker pull hello-world

$ docker run hello-world

$ docker run --name hello-container hello-world 

$ docker rm <CONTAINER ID 1> <CONTAINER ID 2> 

$ docker images | findstr redis

$ docker rm --volumes redis

$ docker rmi redis

🛑 see the following note please.
```

```bash
PS C:\Users\Golestan> docker rmi --help

Usage:  docker rmi [OPTIONS] IMAGE [IMAGE...]

Remove one or more images

Aliases:
  docker image rm, docker image remove, docker rmi

Options:
  -f, --force      Force removal of the image
      --no-prune   Do not delete untagged parent
```

### 4- Pulling and Pushing in Docker 

```bash
$ docker tag hello-world fozouni/hello-de4:v1

$ docker push fozouni/hello-de4:v1
🚀 Done. All guys can use it!
```

### 5- Separating a long command in cli

```bash
# in windows 
$ docker `
> image `
> ls

# in linux
$ docker \
> image \
> ls 
```

### 6- Go inside the running container

```bash
$ docker pull fozouni/absenteeism:first_try

$ docker run -d -p 8501:8501 fozouni/absenteeism:first_try
# port 8501 will goes to 8502 on our local machine

$ docker exec -it <CONTAINER ID> bash

$ cd /
$ cat /etc/os-release 

$ docker run -d <CONTAINER ID>
# -d, --detach Run container in background and print container ID

$ docker logs <CONTAINER ID> 
```

### 7- A magic command

```bash
# Open yor Powershel in admin mode. Then

$ net stop hns

$ net start hns

# These commands will remove the port conflict error.  
```

