# -*- coding: utf-8 -*-

import pytest


def add(a, b):
    return a + b


def test_addition():
    result = add(2, 0)

    assert result == 2

testdata = [
    (2, 0, 2),
    (1, 0, 1),
]

@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    result = add(a, b)

    assert result == expected
