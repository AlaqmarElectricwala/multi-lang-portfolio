from main import validate

def test_valid_addresses():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("1.2.3.4") == True

def test_invalid_range():
    assert validate("256.0.0.1") == False
    assert validate("192.168.1.256") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("275.3.6.28") == False

def test_invalid_format():
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1..2.3") == False
    assert validate("1.2.3.") == False
    assert validate(".1.2.3") == False

def test_leading_zeros():
    assert validate("192.168.001.1") == False
    assert validate("01.2.3.4") == False
    assert validate("1.02.3.4") == False
    assert validate("1.2.003.4") == False
