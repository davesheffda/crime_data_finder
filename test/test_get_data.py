from src.get_data import get_data

def test_function_creates_a_variable_containing_the_date_time():
    assert ininstance(get_data(), str)

# def test_get_data_function_creates_file_name_with_the_date_and_time():
    # pass