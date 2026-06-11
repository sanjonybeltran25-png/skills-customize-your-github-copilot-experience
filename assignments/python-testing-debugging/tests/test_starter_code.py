import pytest

from starter_code import add, safe_divide, format_full_name


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_safe_divide():
    assert safe_divide(10, 2) == 5


def test_format_full_name():
    assert format_full_name("jane", "doe") == "Jane Doe"
    assert format_full_name("  albert", "einstein  ") == "Albert Einstein"


def test_safe_divide_zero():
    with pytest.raises(ValueError):
        safe_divide(10, 0)
