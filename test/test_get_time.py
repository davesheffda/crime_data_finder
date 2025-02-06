from src.get_time import get_time_string
import re


def test_time_function():
    time = get_time_string()
    assert isinstance(time, str)


def test_date_and_time_stored_in_correct_format():
    reg = re.compile(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}")
    time = get_time_string()
    time_element = time[-19:]
    print(time)
    print(time_element)
    print(len(time_element))
    found_time = reg.search(time_element)
    assert found_time
