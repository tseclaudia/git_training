from calc import add

def test_log():
	assert log(100) == 2
	assert log(8, 2) == 3

def test_add():
    assert add(1, 2) == 3