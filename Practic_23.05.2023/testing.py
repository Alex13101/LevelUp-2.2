
import unittest
import pytest

def func(a):
    return a**2
#
# @pytest.mark.parametrize('a', [2,3,5])
# def test_add(a):
#     result = func(a)
#     assert result == a**2
#
#
# @pytest.fixture
# def setup():
#     data = {1: 2}
#     return data
#
# def test_fix(setup):
#     assert setup[1] == 2

# async def asinc_func():
#     print(2)
#     return 1+2
# @pytest.mark.asyncio
# async def test_asinc_func():
#     assert await asinc_func() == 3


class TestOperatins:
    def func(self):
        assert func(6) == 6**2
