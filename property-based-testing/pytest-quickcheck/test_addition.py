# -*- coding: utf-8 -*-

import pytest


def add(a, b):
    return a + b


def test_addition():
    result = add(2, 0)

    assert result == 2

@pytest.mark.randomize(a=int, b=int, ncalls=2)
def test_addition(a, b):
    result = add(a, b)

    assert result == a + b
