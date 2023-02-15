def main():
    greeting = input('Say something: ')
    print(f'${value(greeting)}')


def value(greeting):
    #in case user types space before text and types uppercase(to not check both)
    greeting = greeting.strip().lower()
    #if first word is hello
    if greeting.find('hello') == 0:
        return 0
    #if it starts with h, but not hello
    elif greeting.find('h') == 0:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
