def main():
    #create infinite loop which will break if user's input is correct

    while True:
        try:
            fraction = input('Fraction: ')
            #user will type fraction like 3/4, that's why we should split
            x, y = fraction.split('/')

            #turn strings into ints, if there are no integer(s) value error will be rised
            x = int(x)
            y = int(y)

            #its impossible to fuel tank more than 100%, so if it is, just skip that iteration of the loop
            if x / y > 1:
                raise ValueError
            #obviously we cant divide on 0
            elif y == 0:
                raise ZeroDivisionError

        except:
            #if we have exception just ignore that(just pass), and start loop over
            pass
        else:
            #only if we dont have exception get out of the loop
            break


    #convert that into percentage
    percentage = convert(fraction)

    #give back E, F, or the same percentage
    fullness = gauge(percentage)

    print(fullness)

def convert(fraction):
    x , y = fraction.split('/')
    if not x.isnumeric() or not y.isnumeric():
        raise ValueError
    if y == '0':
       raise ZeroDivisionError
    8/8 becomes 1.0 thats why we need to make it int
    x = int(x)
    y = int(y)
    # return nearest integer  1.1 -> 1   1.6 -> 2
    return round(x/y * 100)


def gauge(percentage):
    #if its almost full
    if percentage >= 99:
        return 'F'
    #if its almost empty
    elif percentage <= 1:
        return 'E'

    #our main case
    return f'{percentage}%'




if __name__ == "__main__":
    main()








