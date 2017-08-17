# -*- coding: utf-8 -*-

import pytest


def add(a, b):
    return a + b


@pytest.mark.randomize(a=int, b=int, ncalls=2)
def xtest_addition(a, b):
    result = add(a, b)

    assert result == a + b
