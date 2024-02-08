from plates import is_valid

def test_first2_alpha():
    assert is_valid("A55555") != True
    assert is_valid("5A5555") != True

def test_min2_max6():
    assert is_valid("A") != True
    assert is_valid("AA55555") != True

def test_num_not_in_middle_and_last():
    assert is_valid("AA5AAA") != True
    assert is_valid("AAAA5A") != True
    assert is_valid("AA55A5") != True

def test_num_in_middle_not_start_zero():
    assert is_valid("AA0555") != True
    assert is_valid("AAAA05") != True
    
def test_no_periods_punct_spaces():
    assert is_valid(" AA5555") != True
    assert is_valid("AA5555 ") != True
    assert is_valid("AA,555") != True
    assert is_valid("AA.555") != True
    assert is_valid("AA-_55") != True