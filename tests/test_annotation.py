def fn(a, b):
    return a + b


def test_int():
    fn(1, 5)


def test_mixed():
    fn(1, 5.0)


def test_string():
    fn("1", "5")
