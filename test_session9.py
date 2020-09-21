import pytest, os, session9



#1
def test_odd_secs():
    k = session9.print_func( add, 10)
    assert k == {'add': 5}