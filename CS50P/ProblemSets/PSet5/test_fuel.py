import fuel
import pytest

def test_convert():
    frac = {"4/4": 100, "0/4": 0, "2/3": 67, "1/3": 33, "1/101": 1}
    for k, v in frac.items():
        assert fuel.convert(k) == v


def test_convert_ValueError():
    with pytest.raises(ValueError):
        fuel.convert("5/4")
        fuel.convert("cat/dog")

def test_convert_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")

def test_gauge():
    g = {1: "E", 0: "E", 100: "F", 99: "F", 42: "42%", }
    for k, v in g.items():
        assert fuel.gauge(k) == v