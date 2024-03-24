from datetime import date
import sys
import inflect

def main():
    delta = birthday(input("Date of birth: "))
    print(sing(delta))

def birthday(bd_string):
    try:
        bd = date.fromisoformat(bd_string)
    except ValueError:
        sys.exit("Invalid Date")
    delta = date.today() - bd
    return delta.days*24*60

def sing(delta):
    p = inflect.engine()
    words = p.number_to_words(delta).capitalize()
    words = words.replace(" and ", " ")
    return words + " minutes"

if __name__ == "__main__":
    main()
