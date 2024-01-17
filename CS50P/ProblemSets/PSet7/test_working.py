from working import convert
import pytest

def test_convert_valid():
    l = ["9 AM to 5 PM", "9 AM to 5:30 PM", "9:30 AM to 5 PM", "9:30 AM to 5:30 PM", "9:30 PM to 5:30 AM"]
    for s in l:
        assert convert(s) in ["09:00 to 17:00", "09:00 to 17:30", "09:30 to 17:00", "09:30 to 17:30", "21:30 to 05:30"]

def test_convert_invalid_format():
    l = ["9 to 5", "9 AM 5 PM", "9 AM - 5 PM", "9 AM", "9:30 PM - 5:30 AM", "nine to five"]
    for s in l:    
        with pytest.raises(ValueError):
            convert(s)

def test_convert_invalid_time():
    l = ["-1 AM to 5 PM", "13 AM to 5 PM", "9 AM to 60 PM", "9 AM to 5:60 PM"]
    for s in l:    
        with pytest.raises(ValueError):
            convert(s)