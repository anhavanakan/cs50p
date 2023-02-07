from working import convert
import pytest

def test_add_00_for_single_digits():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_12am_12pm():
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'

def test_without_word_to():
    with pytest.raises(ValueError):
        convert('9:00 AM 6:00 PM')

def test_minutes_more_than_59():
    with pytest.raises(ValueError):
        convert('9 AM to 11:78 PM')

def test_hours_more_than_12():
    with pytest.raises(ValueError):
        convert('9 AM to 13:78 PM')

def test_blank_text():
    with pytest.raises(ValueError):
        convert('')

def test_minutes_am_pm_in_lowercase():
    with pytest.raises(ValueError):
        convert('9 AM to 11:78 pm')
        convert('9 aM to 11:78 PM')
