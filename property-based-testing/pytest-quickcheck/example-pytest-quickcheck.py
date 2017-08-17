# -*- coding: utf-8 -*-

import pytest

@pytest.mark.randomize(i1=int, i2=int, ncalls=1)
def test_generate_ints(i1, i2):
    pass




@pytest.mark.randomize(
    d1={'x': int, 'y': [str, (int, int)], 'z': {'x': str}}
)
def test_generate_dict(d1):
    pass



@pytest.mark.parametrize("prime", [2, 3, 5])
@pytest.mark.randomize(i1=int, f1=float, ncalls=1)
def test_gen_parametrize_with_randomize_int_float(prime, i1, f1):
    pass


#Python 3
@pytest.mark.randomize(min_num=0, max_num=2, ncalls=5)
def test_generate_int_anns(i1: int):
    pass
