def main():
    str = input("Input: ")
    print("Output:", shorten(str))
    
def shorten(str):
    short = ""
    for l in str:
        if l.lower() not in ["a", "e", "i", "o", "u"]:
            short = short + l
    return short
            
if __name__ == "__main__":
    main()