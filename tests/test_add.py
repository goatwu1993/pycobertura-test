from pycobertura_test.add import add, badNameing


def test_add():
    assert add(1, 2) == 3


def test_bad_naming():
    badNameing()