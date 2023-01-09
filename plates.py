def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #plate should start with 2 letters, if it doesn't return false
    if not s[0].isalpha() and not s[1].isalpha():
        return False

    #plate shold be digit or letter and should contain 2 to 6 characters inclusively
    counter = 0
    for i in s:
        if not i.isalnum():
            return False
        counter += 1
    if 2 > counter or counter > 6:
        return False

    counter = 0
    for i in s:
        if i.isalpha() and counter < len(s) - 1:
            #first number can not be 0
            #if character is letter we should check, is next character 0 or not
            if s[counter + 1] == '0':
                return False
        counter += 1

    #if we have digit in plate after that should me only digits e.g ABC777 - correct  ABC77A - incorrect
    counter = 0
    for i in s:
        if i.isnumeric() and counter < len(s) - 1:
            if s[counter + 1].isalpha():
                return False
        counter += 1
    #if everything is ok return true
    return True

main()
