from plates import is_valid

def main():
    test_leading_2_letters()
    test_characters_2_to_6()
    test_first_number_not_0()
    test_nombers_only_at_the_end()
    test_only_alphanumeric()


def test_leading_2_letters():
    assert is_valid('AA') == True
    assert is_valid('12') == False
    assert is_valid('A1') == False
    assert is_valid('1A') == False
    assert is_valid('A ') == False
    assert is_valid(' A') == False

def test_characters_2_to_6():
    assert is_valid('A') == False
    assert is_valid('ABCDEFGGHG') == False

def test_first_number_not_0():
    assert is_valid('ABC12') == True
    assert is_valid('ABC012') == False

def test_nombers_only_at_the_end():
    assert is_valid('ABC1A') == False

def test_only_alphanumeric():
    assert is_valid('ABC.12') == False
    assert is_valid('ABC  1') == False

if __name__ == '__main__':
    main()
