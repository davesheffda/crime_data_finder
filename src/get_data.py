from datetime import datetime
import ipinfo
import socket
import os
import sys
from urllib.request import urlopen
import re
from dotenv import load_dotenv

load_dotenv()

def getIP():
    d = str(urlopen('http://checkip.dyndns.com/').read())
    ip_address = re.compiler(r'Address: (\d+\.\d+|.|d+\.\d+)').search(d).group(1)
    return

def get_data(ip_address):
    time = f"{datetime.now()}"
    time = time[:22]
    print(f"The current date and time is {time}")
    # hostname = socket.gethostname()
    # ip = socket.gethostbyname(hostname)
    ip = ip_address
    print(f"IP address is {ip}")
    access_token = os.getenv('ACCESS_TOKEN')
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip)
    for key, value in details.all.items():
       print(f"{key}: {value}") 
    # latitude = res.latitude
    # longitude = res.longitude
    # print(f"Latitude -->> {latitude}, Longitude -->> {longitude} ")
    return time


get_data()
