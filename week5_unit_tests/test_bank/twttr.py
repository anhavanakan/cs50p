import sys


def main():
    # for entering the loop
    text = ""
    try:
        # if len is 0, the string is empty
        while len(text) == 0:
            # in that case reprompt the user
            text = input("Input: ")
        # if all is ok do whatever is written below
        text = shorten(text)
    # in case user types ctrl + d or ctlr + c
    except (EOFError, KeyboardInterrupt):
        # go one line below
        print()
        # exit with message
        sys.exit("Oops")
    print(f"Output: {text}")


def shorten(word):
    # for entering the loop
    shortened_word = ""
    for c in word:
        # if vovel just ignore that letter
        if c in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            continue
        # if not add to variable
        shortened_word += c
    # just return
    return shortened_word


if __name__ == "__main__":
    main()
