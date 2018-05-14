# -*- coding: utf-8 -*-

import pytest
from unittest.mock import patch
from unittest.mock import MagicMock, Mock

class ProductionClass(object):
    def method(self):
        pass


def test_magimock_called_with():
    thing = ProductionClass()
    thing.method = MagicMock(return_value=3)

    thing.method(3, 4, 5, key='value')

    thing.method.assert_called_with(3, 4, 5, key='value')


def test_magimock_raises_error():
    mock = Mock(side_effect=KeyError('foo'))

    with pytest.raises(KeyError):
        mock()


def test_mock_called_with():
    mock = Mock()

    mock.method(1, 2, 3)

    mock.method.assert_called_with(1, 2, 3)

def test_patch():
    with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
        thing = ProductionClass()
        thing.method(1, 2, 3)

    mock_method.assert_called_once_with(1, 2, 3)


def test_magicmock_str():
    mock = MagicMock()
    mock.__str__.return_value = 'foobarbaz'
    str(mock)

    mock.__str__.assert_called_with()

from unittest.mock import create_autospec
def test_autospec():
    def function(a, b, c):
        pass

    mock_function = create_autospec(function, return_value='fishy')
    mock_function(1, 2, 3)

    mock_function.assert_called_once_with(1, 2, 3)
    with pytest.raises(TypeError, message="missing a required argument: 'b'"):
        mock_function('wrong arguments')

def test_assert_not_called():
    m = Mock()

    m.hello.assert_not_called()

from unittest.mock import sentinel
def test_sentinel():
    real = ProductionClass()
    real.method = Mock(name="method")
    real.method.return_value = sentinel.some_object

    result = real.method()