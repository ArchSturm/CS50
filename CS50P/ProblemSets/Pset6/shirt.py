import sys
import os.path
from PIL import Image
from PIL import ImageOps


if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments ")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments   ")

extvar1 = os.path.splitext(sys.argv[1])
extvar2 = os.path.splitext(sys.argv[2])

if extvar1[1] == "":
    sys.exit("Invalid input")
elif extvar2[1] != extvar1[1]:
    sys.exit("Invalid output")
else:
    try:
        photo = Image.open(sys.argv[1])
    except:
        sys.exit("Input does not exist")
    
shirt = Image.open("shirt.png")
photo = ImageOps.fit(photo, shirt.size)
photo.paste(shirt, shirt)
photo.save(sys.argv[2])