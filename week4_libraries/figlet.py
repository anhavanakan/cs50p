import sys
from pyfiglet import Figlet
import random

# from module docs
figlet = Figlet()

# get all the fonts in list
fonts = figlet.getFonts()


if len(sys.argv) not in [1, 3]:
    sys.exit("arguments should be 0 or 2")

# if argc is 2, check is 1st argument correct and is font in our list
if len(sys.argv) == 2:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
        pass
    else:
        sys.exit(
            '1st should be "-f" or "--font", and second should be a real font name'
        )

# if we are there that means arguments are OK
text = input("Input: ")

# if font name is specified set that, if not set random one
if len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[2])
else:
    figlet.setFont(font=random.choice(fonts))

# finally convert our text to specified font and print
print(figlet.renderText(text))
