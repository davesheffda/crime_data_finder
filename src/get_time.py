from datetime import datetime


def get_time_string():
    time = f"{datetime.now()}"
    time = time[:19]
    time_string = f"The current date and time is {time}"
    print(time_string)
    return time_string


