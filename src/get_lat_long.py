import ipinfo
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_lat_long():
    """
    Function that uses the ipify api to return the latitude and longitude of a computer using its IP address.

    """
    response = requests.get("https://api.ipify.org?format=json")
    ip_address = response.json()["ip"]
    access_token = os.getenv("ACCESS_TOKEN")
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    lat_long_ip = {}
    lat_long_ip["lat"] = details.latitude
    lat_long_ip["long"] = details.longitude
    lat_long_ip["ip"] = ip_address
    return lat_long_ip
