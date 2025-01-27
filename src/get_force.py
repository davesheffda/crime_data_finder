import requests
from src.get_lat_long import get_lat_long

def get_force():
    '''
    Function that uses the police API to retrieve the unique force code and force specific team identifier for a british police base on the latitute and longitude
    '''
    lat_long = get_lat_long()
    response = requests.get(f"https://data.police.uk/api/locate-neighbourhood?q={lat_long['lat']},{lat_long['long']}")
    force_data = response.json()
    print(f'Your local police force is {force_data['force']}')
    print(f'The force specific team identifier for your neighbourhood is {force_data['neighbourhood']}')
    return force_data