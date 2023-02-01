import re


def main():
    #will print True or False
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    try:
        #groups are in ip.groups()
        for i in ip.groups():
            #range of ip number digits is 0-255
            #and its a string, thats why we need to make it int for comparison
            if int(i) > 255:
                return False

    # AttributeError raises when there is non numeric value somewhere between dots
    except AttributeError:
        return False
    #if we are there all is good
    return True


if __name__ == "__main__":
    main()
