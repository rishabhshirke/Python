import pytest

def func(x):
    return x+5


def test_method():
    assert func(3) == 8

class TestClass:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        self.value = 2
        assert self.value == 2