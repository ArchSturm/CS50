from plates import is_valid

def test_is_valid_true():
    plates = ["AA", "AAA111", "CS50"]
    for plate in plates:
        assert is_valid(plate) == True

def test_is_valid_false():
    plates = ["A1", "CS50P", "CS50P2", "CS05", "A", "AAAAAAA", "PI3.14"]
    for plate in plates:
        assert is_valid(plate) == False
