from __future__ import annotations
from dataclasses import FrozenInstanceError

import pytest
from wc.result import Err

def test_value():
    assert Err(1).error == 1

def test_immutability():
    err = Err(1)
    with pytest.raises(FrozenInstanceError):
        err.error = 2

def test_map():
    f = lambda a: a + 1
    Err(1).map(f) == Err(1)

def test_bind():
    f = lambda a: a + 1
    assert Err(1).bind(f) == Err(1)

def test_map_err():
    f = lambda a: a + 1
    assert Err(1).map_err(f) == Err(2)

