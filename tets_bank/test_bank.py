from bank import value

def main():
    test_hello()
    test_h_but_not_hello()
    test_first_letter_isnt_h()


def test_hello():
    assert value('Hello, davif') == 0

def test_h_but_not_hello():
    assert value('hi, bro') == 20


def test_first_letter_isnt_h():
    assert value('nice to meet you') == 100

if __name__ == '__main__':
    main()
