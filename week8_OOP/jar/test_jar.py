from jar import Jar
import pytest

def test_init():
    # we can access to attribute without instantiating an object
    assert Jar(7).capacity == 7
    assert Jar().capacity == 12

    # pass capsys so that you can use it
def test_str(capsys):
    jar = Jar(20)
    jar.deposit(3)
    print(jar)
    # capsys.readouterr will get what has printed and return `output` and  `error`  in `out` and `err` 
    captured = capsys.readouterr()
    # ofc we need output 
    assert captured.out == '🍪🍪🍪\n'


def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        assert jar.withdraw(10)

def test_deposit():
    jar = Jar(10)
    jar.deposit(1)
    assert jar.size == 1

    with pytest.raises(ValueError):
        assert jar.deposit(20)
