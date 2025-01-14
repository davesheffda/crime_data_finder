from src.get_data import get_data
import re


def test_function_creates_a_list_containing_the_date_time_as_the_first_element():
    returned_data = get_data()
    assert isinstance(returned_data[0], str)


def test_date_and_time_stored_in_correct_format():
    reg = re.compile(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{2}")
    returned_data = get_data()
    found_time = reg.search(returned_data[0])
    assert found_time


def test_latitude_and_longitude_returned():
    returned_data = get_data()
    assert isinstance(returned_data, list)
    assert len(returned_data) == 3

# def test_latitude_and_longitude_are_in_correct_format():

