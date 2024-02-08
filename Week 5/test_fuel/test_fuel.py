import pytest
from fuel import convert, gauge
from fuel import gauge

def test_convert_str():
    with pytest.raises(ValueError):
        convert("5/s")
        convert("s/5") == ValueError
        convert("s/s") == ValueError

def test_convert_divide_zero():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_convert_no_slash():
    with pytest.raises(ValueError):
        convert("5*3")
        convert("5&3") == ValueError
        convert("5!3") == ValueError
        convert("5@3") == ValueError
        convert("5.3") == ValueError
        convert("5,3") == ValueError
        convert("5s3") == ValueError

def test_normal():
    assert convert("10/40") == 25
    assert gauge(25) == "25%"
    assert convert("20/40") == 50
    assert gauge(50) == "50%"
    assert convert("30/40") == 75
    assert gauge(75) == "75%"

def test_full():
    assert convert("40/40") == 100
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_empty():
    assert convert("1/100") == 1
    assert gauge(1) == "E"
    assert gauge(0) == "E"