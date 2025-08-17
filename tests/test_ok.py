from dataclasses import FrozenInstanceError

import pytest
from wc.result import Err, Ok

def test_value():
    assert(Ok(1337).value == 1337)

def test_immutability():
    x = Ok(1)
    with pytest.raises(FrozenInstanceError):
        x.value = 2

def test_map():
    increment = lambda n: n + 1
    assert Ok(1).map(increment) == Ok(2)

def test_identity():
    identity = lambda a: a
    assert Ok("a").map(identity) == Ok("a")

def test_composition():
    f = lambda n: n + 2
    g = lambda n: n * 3
    left = Ok(5).map(f).map(g)
    right = Ok(5).map(lambda a: g(f(a)))
    assert left == right

def test_bind():
    to_ok = lambda n: Ok(n * 10)
    assert Ok(3).bind(to_ok) == Ok(30)

def test_right():
    assert Ok("x").bind(Ok) == Ok("x")

def test_left():
    f = lambda s: Ok(s + "!")
    assert Ok("hi").bind(f) == f("hi")

def test_assosiativity():
    f = lambda n: Ok(n + 1)
    g = lambda n: Ok(n * 2)

    m = Ok(10)

    left = m.bind(f).bind(g)
    right = m.bind(lambda x: f(x).bind(g))

    assert right == left