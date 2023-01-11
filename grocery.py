list = dict()
while True:
    try:
        item = input().lower()
        list[item] += 1
    except KeyError:
        list[item] = 1
    except EOFError:
        print()
        for i in list:
            print(f'{list[i]} {i.upper()}')

        break
