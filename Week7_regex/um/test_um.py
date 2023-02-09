from um import count

def test_one_um():
    assert count('um') == 1

def test_um_inside_a_word():
    assert count('umbrella') == 0
    assert count('gum') == 0
    assert count('yummy') == 0

def test_punctuation():
    assert count('um..') == 1
    assert count('.um') == 1

def test_case_insensitive():
    assert count('UM') == 1
    assert count('uM') == 1
    assert count('Um') == 1
