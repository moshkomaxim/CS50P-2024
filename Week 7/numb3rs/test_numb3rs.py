from numb3rs import validate


def test_nums():
    assert validate("1") == False
    assert validate("1.") == False
    assert validate("1.1") == False
    assert validate("1.1.") == False
    assert validate("1.1.1") == False
    assert validate("1.1.1.") == False

def test_grammatical():
    assert validate("abc.abc.abc.abc") == False
    assert validate("cat") == False
    assert validate("255,255,255,255") == False
    assert validate("1s1s1s1") == False

def test_out_range():
    assert validate("287.200.200.200") == False
    assert validate("200.287.200.200") == False
    assert validate("287.200.287.200") == False
    assert validate("287.200.200.287") == False
    assert validate("1111.2222.3333.4444") == False

def test_ok():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("229.229.229.229") == True
    assert validate("149.149.149.149") == True