from twttr import shorten

def test_shorten():
    sl = {"Hello, world": "Hll, wrld", "Twitter": "Twttr", "TWITTER": "TWTTR", "CS50": "CS50", "!@#$%^&*()_+-=/": "!@#$%^&*()_+-=/"}
    for s, ss in sl.items():
        assert shorten(s) == ss