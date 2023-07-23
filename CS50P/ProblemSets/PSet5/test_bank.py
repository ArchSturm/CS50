from bank import value

def test_value():
    test = {"Hello": 0, "Hey": 20, "Wassap": 100, "hi": 20, "": 100, "123": 100}
    for k, v in test.items():
        assert value(k) == v