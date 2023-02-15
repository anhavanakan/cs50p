import random
import sys
def main():
    #get the highest number from the user
    top_number = get_number('Level: ')

    #random number between range of 1 and typed top number
    rand_number = random.randint(1, top_number)

    #to enter the loop and being sure it isn't equel to random number
    guessed_number = -1

    while rand_number != guessed_number:
        guessed_number = get_number('Guess: ')

        if  guessed_number > rand_number:
            print('Too large!')
        elif guessed_number < rand_number:
            print('Too small!')


    print('Just right!')
    sys.exit()


def get_number(text):
    #for entering the loop
    n = -1

    while n < 0:
        n = input(text)
        #if its numeric make it int, if not make it '-1' for comparing with 0 and 'continue'
        if n.isnumeric():
            n = int(n)
        else:
            n = -1
            continue
        #if its natural number we are good to go, just break the loop
        if n > 0:
            break
        else:
            #else set it to -1 to enter the loop again
            n = -1
            continue
    #if we are there n is definitely natural number
    return n


main()



