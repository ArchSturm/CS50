from um import count

def test_count_1():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("...um...") == 1
    assert count("Um, thanks for the album.") == 1

def test_count_2():
    assert count("um um") == 2
    assert count("um-um") == 2
    assert count("Um, thanks, um...") == 2
    assert count("um, so yummy, hum! umum um.") == 2
    
def test_count_0():
    assert count("ummm") == 0
    assert count("umum") == 0
    assert count("yummy") == 0
    assert count("bum, mum") == 0
    assert count("1337") == 0