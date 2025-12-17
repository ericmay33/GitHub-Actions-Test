import pytest

def test_always_fails():
    """This test is designed to fail"""
    assert 1 == 2, "Expected failure: 1 does not equal 2"

def test_division_by_zero():
    """This test will raise an exception"""
    result = 10 / 0

def test_assertion_error():
    """Another failing test"""
    expected = "hello"
    actual = "goodbye"
    assert expected == actual, f"Expected '{expected}' but got '{actual}'"