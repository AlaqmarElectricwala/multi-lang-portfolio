import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar2 = Jar(5)
    assert jar2.capacity == 5
    assert jar2.size == 0

    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("ten")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(2)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    jar.withdraw(2)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
