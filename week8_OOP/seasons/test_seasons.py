import pytest
from seasons import date_to_words

def test_sysexit():
    with pytest.raises(SystemExit):
        date_to_words("January 1, 1999")
        date_to_words("2001.01.03")

#we could use other version of test which is below


# def test_sysexit():
#     with pytest.raises(SystemExit, match='Invalid date') as error:
#         date_to_words("January 1, 1999")
#     assert error.type == SystemExit
