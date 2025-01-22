import ipinfo
import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_lat_long():
    response = requests.get("https://api.ipify.org?format=json")
    ip_address = response.json()["ip"]
    print(f"Your IP address is {ip_address}")
    access_token = os.getenv("ACCESS_TOKEN")
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    lat_long = {}
    lat_long['lat'] = details.latitude
    lat_long['long'] = details.longitude
    print(f"Your latitude is -->> {lat_long['lat']}, Your longitude is -->> {lat_long['long']} ")
    return lat_long

