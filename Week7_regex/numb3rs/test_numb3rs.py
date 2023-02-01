from numb3rs import validate
def test_letters():
    assert validate("a") == False
    assert validate("1.1.1.a") == False
    assert validate("a.a.a.1") == False


def test_numbers():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("275.10.15.7") == False
    assert validate('1.1.1') == False
    assert validate("1.1.1.1.1") == False
    assert validate('1.1.1.390') == False
