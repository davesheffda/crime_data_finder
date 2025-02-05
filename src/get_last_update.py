import requests

def get_last_update():
    '''
    Checks the Police API and returns date when the API was last updated

    Args: None
    Returns: Date in string format 
    Examples:
        get_last_update()
        # "The last time the Police API was update was 2024-11-01"
    '''
    response = requests.get("https://data.police.uk/api/crime-last-updated")
    print(response.json())
    last_update = response.dumps()
    return last_update

get_last_update()