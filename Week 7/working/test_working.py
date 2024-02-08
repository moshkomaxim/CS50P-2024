import pytest
from working import convert


def test_range():
    with pytest.raises(ValueError):
        convert("13:00 AM to 02:00 PM")
        convert("02:00 AM to 13:00 PM")
        convert("19:00 AM to 19:00 PM")
        convert("25:00 AM to 25:00 PM")
        convert(" to ")
        convert("to ")
        convert(" to")

def test_invalid_time_format():
    with pytest.raises(ValueError):
        convert(' 1212 to 1111 ')

def test_invalid_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_hyphen():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_short():
    assert convert("9 AM to 12 PM") == "09:00 to 12:00"

