
def increment(x):
    return x + 1

def test_increment():
    assert increment(3) == 4

def test_increment_fail():
    assert increment(3) == 4

test_increment()
test_increment_fail()