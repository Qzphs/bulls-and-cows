import pytest

from game import Code
from tests.mock_randomiser import MockRandomiser


def test_mock_randomiser():
    randomiser = MockRandomiser()
    randomiser.bools = [True, False]
    randomiser.codes = [Code("1234"), Code("2345")]
    assert randomiser.random_bool()
    assert not randomiser.random_bool()
    assert randomiser.random_code().digits == "1234"
    assert randomiser.random_code().digits == "2345"
