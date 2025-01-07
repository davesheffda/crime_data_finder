from datetime import datetime
import os
import ipinfo
import requests
from dotenv import load_dotenv

load_dotenv()


def get_data():
    time = f"{datetime.now()}"
    time = time[:22]
    print(f"The current date and time is {time}")
    response = requests.get('https://api.ipify.org?format=json')
    ip_address = response.json()['ip']
    print(f"IP address is {ip_address}")
    access_token = os.getenv('ACCESS_TOKEN')
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    for key, value in details.all.items():
       print(f"{key}: {value}") 
    # latitude = res.latitude
    # longitude = res.longitude
    # print(f"Latitude -->> {latitude}, Longitude -->> {longitude} ")
    return time


get_data()
