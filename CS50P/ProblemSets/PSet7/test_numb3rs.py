from numb3rs import validate

def test_validade_true():
    ip = ["255.255.255.255", "0.0.0.0", "198.168.0.12", "0.1.10.100"]
    for i in ip:
        assert validate(i) == "True"
        
def test_validate_false():
    ip = ["256.256.256.256", "255.255", ".255.255.255", ".255.255.255.255", "255.255.255.255.", "275.275.275.275", "255.255.255.2555", "cat"]
    for i in ip:
        assert validate(i) == "False"