from pyfiglet import Figlet
import sys
import random

#f = font
#s = text

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            f = sys.argv[2]
        else:
            sys.exit("Invalid font")
    else:
        sys.exit("Invalid argument")
figlet.setFont(font=f)
print("Output:\n" + figlet.renderText(input("Input: ")))
