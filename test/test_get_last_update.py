from src.get_last_update import get_last_update

def test_function_returns_string():
    assert isinstance(get_last_update(), str)
