from src.get_data import get_data


def test_function_returns_dictionary():
    assert isinstance(get_data(), list)
