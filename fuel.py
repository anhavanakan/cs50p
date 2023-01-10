#create infinite loop which will break if user's input is correct
while True:
    try:
        fullness = input('Fraction: ')
        #user will type fraction like 3/4, that's why we should split
        x, y = fullness.split('/')

        #turn strings into ints
        x = int(x)
        y = int(y)

        #its impossible to fuel tank more than 100%, so if it is, just skip that iteration of the loop
        if x / y > 1:
            continue
        elif x / y >= 0.99:
            print('F')
        elif x / y <= 0.01:
            print('E')
        else:
            #get percent from decimal value
            print(f'{round((x / y) * 100)}%')
    except (ValueError, ZeroDivisionError):
        #if we have exception just ignore that(just pass)
        pass
    else:
        #only if we dont have exception break the loop, and end the program
        break
