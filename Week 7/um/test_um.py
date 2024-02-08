from um import count

def test_in_word():
    assert count("Num of pum is under plum") == 0

def test_with_end():
    assert count("um, um. um! um- um= um?") == 6

def test_case():
    assert count("Um") == 1

def test_spaces():
    assert count("          um           um       um            um string         um") == 5