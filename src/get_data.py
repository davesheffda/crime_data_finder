import datetime
from datetime import datetime
from ip2geotools.databases.noncommercial import DbIpCity
import socket

def get_data():
    time = f'{datetime.now()}'
    print(time)
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f'IP address is {ip}')
    res = DbIpCity.get(ip, api_key="free")
    latitude = res.latitude
    longitude = res.longitude
    print(f'Latitude -->> {latitude}, Longitude -->> {longitude} ')
    return time
    

get_data()