from src.get_nbhd import get_nbhd

def test_function_returns_dictionary():
    assert isinstance(get_nbhd(), dict)