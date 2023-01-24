from fuel import convert, gauge
import pytest

def test_f_and_e():
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    #it should be with '%'


def test_percent_sign():
    assert gauge(90) != '90'


#no need to check for wrong input, becouse it was checked in main function
def test_conversion():
    assert convert('1/4') == 25
    assert convert('1/1') == 100
    assert convert('1/100') == 1


#to check is function raises errors we should use pytest libray as follows
#above 'with' write expression you want to check
def test_exceptions():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('a/1')
