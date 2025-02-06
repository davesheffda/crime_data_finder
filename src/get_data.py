from src.get_time import get_time_string
from src.get_lat_long import get_lat_long
from src.get_force import get_force
from src.get_last_update import get_last_update
import requests
import pprint


import requests


def get_data():
    time = get_time_string()
    last_update = get_last_update()
    lat_long_ip = get_lat_long()
    print(f"Your IP address is {lat_long_ip['ip']}")
    print(
        f"Your latitude is -->> {lat_long_ip['lat']}, Your longitude is -->> {lat_long_ip['long']} "
    )
    get_force()
    latitude = lat_long_ip["lat"]
    longitude = lat_long_ip["long"]
    response = requests.get(
        f"https://data.police.uk/api/crimes-street/all-crime?lat={latitude}&lng={longitude}"
    )
    sl_crimes = response.json()
    pprint.pp(
        "Recent street level crimes within a mile of your current location are........."
    )
    pprint.pp(sl_crimes)
    return sl_crimes


get_data()
