import pytest
from seasons import getDate


def test_getDate_str():
    with pytest.raises(SystemExit):
        getDate("ssssss")
        getDate("sssss sssssssss sssssss")
        getDate("ssss-ss-ss")

def test_getDate_range():
    with pytest.raises(SystemExit):
        assert getDate("2010-13-10")
        assert getDate("2010-12-32")

def test_getDate_mark():
    with pytest.raises(SystemExit):
        getDate("2010/12/12")
        getDate("2010=12=12")
        getDate("2010\12\12")
        getDate("20101212")

