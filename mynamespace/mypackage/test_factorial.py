from mynamespace.mypackage.factorial import factorial

def test_factorial():
    """Tests factorial to conform to the definition.
    """
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
