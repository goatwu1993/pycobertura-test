import pytest

from pycobertura_test.dummy_square import dummy_square


@pytest.mark.parametrize("i, expected", [(1, 1), (2, 4)])
def test_dummy_square(i, expected):
    assert dummy_square(i) == expected
