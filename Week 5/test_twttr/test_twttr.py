from twttr import shorten


def test_A():
    assert shorten("A") != "A"

def test_E():
    assert shorten("E") != "E"

def test_I():
    assert shorten("I") != "I"

def test_O():
    assert shorten("O") != "O"

def test_U():
    assert shorten("U") != "U"

def test_AEIOU():
    assert shorten("AEIOU") != "AEIOU"

def test_spaces():
    assert shorten("  Hello  World  ") == "  Hll  Wrld  "

def test_case():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"

def test_nums():
    assert shorten("1234567890") == "1234567890"

def test_punct():
    assert shorten(",.") == ",."