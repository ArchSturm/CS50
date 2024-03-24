import seasons
import pytest

def test_birthday():
    assert seasons.birthday("2000-01-01") == 12732480
    assert seasons.birthday("2023-03-18") == 525600
    with pytest.raises(SystemExit):
        seasons.birthday("2023-03-32")
        seasons.birthday("2023, 03, 18")
        seasons.birthday("2023-03-18 00:00:00")
        seasons.birthday("")
        seasons.birthday("cat")
    
def test_sing():
    assert seasons.sing(12732480) == "Twelve million, seven hundred thirty-two thousand, four hundred eighty minutes"
    assert seasons.sing(525600) == "Five hundred twenty-five thousand, six hundred minutes"