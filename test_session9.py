import pytest, os, session9



#1
def test_odd_secs():
    k = session9.print_func( func = add, sec = 10)
    assert k == {'add': 5}