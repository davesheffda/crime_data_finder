from src.get_time import get_time_string
from src.get_lat_long import get_lat_long
from src.get_force import get_force


import requests


def get_data():
    get_time_string()
    lat_long_ip = get_lat_long()
    print(f"Your IP address is {lat_long_ip['ip']}")
    print(f"Your latitude is -->> {lat_long_ip['lat']}, Your longitude is -->> {lat_long_ip['long']} ")
    get_force()
    return


get_data()
