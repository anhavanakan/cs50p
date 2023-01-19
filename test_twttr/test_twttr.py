from twttr import shorten

def main():
    test_lowercase()
    test_uppercase()
    test_lower_and_upper()
    test_numbers()
    test_punctuation()

def test_lowercase():
    assert shorten('twitter') == 'twttr'

def test_uppercase():
    assert shorten('TWITTER') == 'TWTTR'

def test_lower_and_upper():
    assert shorten('twItTeR') == 'twtTR'

def test_numbers():
    assert shorten('123bA') == '123b'

def test_punctuation():
    assert shorten('Hi! I am Artur.') == 'H!  m rtr.'


if  __name__ == '__main__':
    main()
