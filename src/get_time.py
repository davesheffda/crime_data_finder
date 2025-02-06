from datetime import datetime


def get_time_string():
    """
    function which obtains the current date and time, revises the format and outputs it as a string
    """
    time = f"{datetime.now()}"
    time = time[:19]
    time_string = f"The current date and time is {time}"
    print(time_string)
    return time_string
