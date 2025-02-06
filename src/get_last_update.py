import requests

def get_last_update():
    '''
    Checks the Police API and returns date when the API was last updated

    Args: None
    Returns: Date in string format 
    Examples:
        get_last_update()
        # "The police API data was last updated on 2024-11-01"
    '''
    response = requests.get("https://data.police.uk/api/crime-last-updated")
    last_update = response.json()
    last_update_date = last_update['date']
    print(f'The police API data was last updated on {last_update_date}')
    return last_update

get_last_update()