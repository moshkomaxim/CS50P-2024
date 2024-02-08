from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello world") == 0

def test_h():
    assert value("horse") == 20
    assert value("human world") == 20

def test_other():
    assert value("World human") == 100
    assert value("People inside") == 100

def test_space():
    assert value("  hello  ") == 0
    assert value("  horse  ") == 20
    assert value("  World human  ") == 100

def test_case():
    assert value("HELLO") == 0
    assert value("HORSE") == 20
    assert value("WORLD HUMAN") == 100

