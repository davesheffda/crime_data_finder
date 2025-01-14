from datetime import datetime
import os
import ipinfo
import requests
from dotenv import load_dotenv

load_dotenv()


def get_data():
    time = f"{datetime.now()}"
    time = time[:19]
    print(f"The current date and time is {time}")
    response = requests.get("https://api.ipify.org?format=json")
    ip_address = response.json()["ip"]
    print(f"Your IP address is {ip_address}")
    access_token = os.getenv("ACCESS_TOKEN")
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    latitude = details.latitude
    longitude = details.longitude
    print(f"Your latitude is -->> {latitude}, Your longitude is -->> {longitude} ")
    return [time, latitude, longitude]


get_data()
