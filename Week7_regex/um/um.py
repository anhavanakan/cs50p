import re


def main():
    print(count(input("Text: ")))


def count(s):
    #'\b\ is boundery, that means in this pattern I am searching for 'um' not 'num' or 'umn'
    ums_list = re.findall(r'\bum\b',  s, re.IGNORECASE)
    #findall returns all finded things to a list
    #then we return length of that list
    return len(ums_list)



if __name__ == "__main__":
    main()
