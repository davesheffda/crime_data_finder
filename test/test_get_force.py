from src.get_force import get_force


def test_function_returns_dictionary():
    assert isinstance(get_force(), dict)


def test_function_returns_dictionary_with_force_and_neighbourhood_keys():
    result = get_force()
    print(result["force"])
    print(result["neighbourhood"])
    assert "force" in result
    assert "neighbourhood" in result
