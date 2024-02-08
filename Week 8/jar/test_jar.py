import pytest
from jar import Jar


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar(0)
    with pytest.raises((ValueError, TypeError)):
        jar = Jar("s")
    with pytest.raises((ValueError, TypeError)):
        jar = Jar("One")


def test_str():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5)
    assert str(jar) == "🍪" * 6


def test_deposit():
    jar = Jar()
    jar.deposit(0)
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12

    with pytest.raises(ValueError):
        jar.deposit(1)
    with pytest.raises(ValueError):
        jar.deposit(50)
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises((ValueError, TypeError)):
        jar.deposit("-5")
    with pytest.raises((ValueError, TypeError)):
        jar.deposit("5")
    with pytest.raises((ValueError, TypeError)):
        jar.deposit("Five")


def test_withdraw():
    jar = Jar()
    jar.deposit(9)
    assert jar.size == 9
    jar.withdraw(5)
    assert jar.size == 4
    jar.withdraw(3)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
    with pytest.raises(ValueError):
        jar.withdraw(50)

def test_normal():
    test_jar = Jar()
    str(test_jar) == ""
    test_jar.deposit(5)
    str(test_jar) == "🍪" * 5
    test_jar.deposit(6)
    str(test_jar) == "🍪" * 11
    test_jar.withdraw(9)
    str(test_jar) == "🍪" * 2
