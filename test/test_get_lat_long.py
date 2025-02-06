from src.get_lat_long import get_lat_long


def test_latitude_and_longitude_returned_as_dictionary():
    returned_data = get_lat_long()
    assert isinstance(returned_data, dict)
    assert len(returned_data) == 3


def test_latitude_and_longitude_are_in_correct_format():
    lat_long = get_lat_long()
    print(lat_long)
    assert isinstance(lat_long["lat"], str)
    assert isinstance(lat_long["long"], str)
    latitude = float(lat_long["lat"])
    longitude = float(lat_long["long"])
    assert isinstance(latitude, float)
    assert isinstance(longitude, float)
    assert longitude >= -180 and longitude <= 180
    assert latitude >= -90 and latitude <= 90
