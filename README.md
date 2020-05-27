## SSH Servers Dynamic Multi-Threads Bruteforce Password Cracker in Python

 ### requirements:

install virtual env with:
- paramiko==2.7.1
- colorama==0.4.1

Instructions:

###### usage: hack.py [-h] [--user USER] [--max MAX] [-l] [-u] [-d] [-p] host

positional arguments:
-  host               Hostname or IP Address of SSH Server to bruteforce.

optional arguments:
-  -h, --help         show this help message and exit
-  --user USER        Username for host, default = root
-  --max MAX          Maximal len of password default = 14
-  -t THREADS, --threads THREADS
                        Number of threads, default = 1
-  -l, --lowercase    Password generator will include lowercase
-  -u, --uppercase    Password generator will include uppercase
-  -d, --digits       Password generator will include digits
-  -p, --punctuation  Password generator will include punctuation


### Examples of usage:

to run ssh password cracker:
- as root@127.0.0.1 
- input max len of password as 2 characters
- operate on 5 threads
- check combinations of password including lowercase and uppercase only

python3 hack.py 127.0.0.1 --user root --max 2 -t 5 -l -u

##### After finding a password the result will be saved in newly created file password.txt


