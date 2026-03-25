import os
from threading import Thread
from time import sleep
import subprocess
import sys
import socket

def get_local_ip():
    # Get the local machine's hostname
    hostname = socket.gethostname()
    # Get the IP address of the hostname
    ip_address = socket.gethostbyname(hostname)
    return ip_address

local_ip = get_local_ip()
print("Local IP Address:", local_ip)
def runserver():
    # os.system(f'python manage.py runserver {192.168.11.134}:8000')
    os.system(f'python manage.py runserver {local_ip}:8000')

def lunchchrome():
    # ensure the django server is up and running
    sleep(2)
    # get ipv4 address
    # os.system('start chrome http://192.168.1.135:8000')
    os.system(f'start chrome http://{local_ip}:8000')
t1=Thread(target=runserver)

t2=Thread(target=lunchchrome)

t1.start()
t2.start()