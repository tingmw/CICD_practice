from calculate import add_func, sub_func


def test_add_func():
    assert add_func(1, 2) == 3
    assert add_func(0, 0) == 0
    assert add_func(-1, -2) == -3


def test_sub_func():
    assert sub_func(2, 1) == 1
    assert sub_func(0, 0) == 0
    assert sub_func(-2, -1) == -1