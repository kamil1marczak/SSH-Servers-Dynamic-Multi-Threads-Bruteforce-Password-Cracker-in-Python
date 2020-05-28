# SSH Servers Dynamic Multi-Threads Bruteforce Password Cracker in Python
> Simple but powerful tool to crack passwords of ssh servers

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Instructions](#instructions)
* [Code Examples](#code-examples)
* [Status](#status)
* [Contact](#contact)

## General info
The project is motivated by my desire to develop my skills in pentesting, TCP/IP and general python skills. Feel free to copy but use it in ethical way only ;) 

## Technologies
* colorama==0.4.1
* paramiko==2.7.1

## Setup
execute from bash terminal: `source install.sh` script from general folder will install and activate virtual env  

## Instructions
To execute help: `python3 hack.py -h`

It will return:
```
usage: hack.py [-h] [--user USER] [--max MAX] [-l] [-u] [-d] [-p] host

positional arguments:
  host               Hostname or IP Address of SSH Server to bruteforce.

optional arguments:
  -h, --help         show this help message and exit
  --user USER        Username for host, default = root
  --max MAX          Maximal len of password default = 14
  -t THREADS, --threads THREADS
                        Number of threads, default = 1
  -l, --lowercase    Password generator will include lowercase
  -u, --uppercase    Password generator will include uppercase
  -d, --digits       Password generator will include digits
  -p, --punctuation  Password generator will include punctuation
```


## Code Examples
to run ssh password cracker:
- as root@127.0.0.1 
- determine password no longer than 2 characters
- operate on 5 threads
- check combinations of password including lowercase and uppercase only

`python3 hack.py 127.0.0.1 --user root --max 2 -t 5 -l -u`

After finding a password the result will be saved in newly created file password.txt

## Status
Project is: finished, I am looking for new inspirations, please reach me for that purpose/ suggestions (email below)

## Contact
Created by @kamil1marczak - kamil1marczak@gmail.com - feel free to contact me!
