def convert(str):
    emoticon = str.replace(":)", "🙂").replace(":(", "🙁")
    return emoticon

def main():
    str = input()
    emoticon = convert(str)
    print(emoticon)

main()