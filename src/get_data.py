from src.get_time import get_time_string
from src.get_lat_long import get_lat_long


import requests


def get_data():
    time = get_time_string()
    lat_long = get_lat_long()
    return [time, lat_long[0], lat_long[1]]


get_data()
