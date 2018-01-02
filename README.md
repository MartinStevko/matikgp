# Matik GP
Django project for correspondence seminars. Grand Prix of winter Matik 2018.

## Requirements installation

 - Python (3 or later, version 3.6.0 recommended)
 - Django (version 2.0)
 - virtual enviroment

### Windows machine
Install Python from https://www.python.org/downloads/ and then in CMD type:

```cmd
py -m pip install Django==2.0
```
```cmd
py -m pip install virtualenv
```
### Linux machine
In Bash type:

```bash
sudo apt install Python
```
```bash
sudo apt install pip
```
```bash
python3 -m pip install Django==2.0
```
```bash
python3 -m pip install virtualenv
```

## Server setup for local network

You have to get through local setup only once (per a project).

### Windows machine

In CMD:
Create virtual enviroment
```cmd
py -m venv ENV_NAME
```

### Linux machine

In Terminal:
Create virtual enviroment
```cmd
virtualenv ENV_NAME
```
and allow remote acces for desired port:
```bash
iptables -I INPUT -p tcp -m tcp --dport PORT_NUMBER -j ACCEPT
```

## Run server

Don't forget to remove all data from files `zaciatok.txt` and `koniec.txt` in `matikgp\setup` directory before starting server.

### Windows machine

In CMD:
1. Go to matikgp directory
2. Activate your virtual environment:
```cmd
ENV_NAME\Scripts\activate
```
3. Run server on your desired port:
```cmd
python manage.py runserver 0.0.0.0:PORT_NUMBER
```

### Linux machine

1. Login as root user
In Terminal:
2. Go to matikgp directory
3. Activate your virtual environment:
```bash
source ENV_NAME/bin/activate
```
4. Run server on your desired port:
```bash
python manage.py runserver 0.0.0.0:PORT_NUMBER
```
