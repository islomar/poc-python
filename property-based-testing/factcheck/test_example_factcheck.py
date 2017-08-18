# -*- coding: utf-8 -*-

from factcheck import *

@forall(n=ints(-3, 4))
def test_ints_generates_ints_between_min_and_max_inclusive(n):
    assert -3 <= n <= 4
