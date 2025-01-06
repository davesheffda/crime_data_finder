from src.get_data import get_data


def test_function_creates_a_variable_containing_the_date_time():
    assert isinstance(get_data(), str)


def test_date_and_time_stored_in_correct_format():
    reg = re.compile("\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{2}")
    time = get_data()
    found_time = reg.search(time)
    assert found_time

