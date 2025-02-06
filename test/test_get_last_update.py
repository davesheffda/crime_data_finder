from src.get_last_update import get_last_update

def test_function_returns_dict():
    assert isinstance(get_last_update(), dict)

def test_function_returns_dictionary_with_date_key():
    test_date = get_last_update()
    assert 'date' in test_date

def test_function_returns_dictionary_with_string_in_date_key():
    test_date = get_last_update()
    assert isinstance(test_date['date'], str)