from src.get_data import get_data, get_time_string, get_lat_long
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


def test_latitude_and_longitude_returned_as_dictionary():
    returned_data = get_lat_long()
    assert isinstance(returned_data, dict)
    assert len(returned_data) == 2


# def test_latitude_and_longitude_are_in_correct_format():
#     returned_data = get_lat_long()
#     assert returned_data
