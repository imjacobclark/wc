from wc.result import Err, Ok

def test_bind_ok_err():
    to_err = lambda n: Err(n)
    assert Ok(3).bind(to_err) == Err(3)

