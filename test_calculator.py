from calculator import add, subtract, multiply, divide

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_multiply():
	assert multiply(3, 2) == 6

def test_subtract():
	assert subtract(6, 3) == 3

def test_negitive_addition():
	a, b = -5, 2

	result = add(a, b)

	assert result == -3
