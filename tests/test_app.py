from myapp.app import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 3) == 9

def test_divide():
    assert divide(10, 2) == 5
