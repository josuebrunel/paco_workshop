# How to setup the server

### Requirements

```shell
$ sudo aptitude install virtualenvwrapper
$ sudo aptitude install python-pip
```
then reload your session to setup **virtualenvwrapper**

### Downloads the package ( Git or Not )

#### With **git**
```shell
$ cd workspace
$ git clone https://github.com/josuebrunel/paco_workshop.git
$ cd paco_workshopkshop
```

### Without git 
Download the package from web github interface :wink:


### Create a virtual environment and install packages

```shell
$ mkvirtualenv server
(server)$ 
(server)$ cd ~/workspace/paco_workshop 
(server)$ pip install -r server/requirements.txt 
```

### Run server
```shell
(server)$ ./run.py
```
