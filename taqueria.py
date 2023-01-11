menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#total money for meals
total = 0

while True:
    try:
        #titling input as in menu and stripping just in case
        item = input('Item: ').title().strip()
        #if item in menu add price of that to the total, else skip this 1 iteration of the loop
        if item in menu:
            total += menu[item]
        else:
            continue
    #if user ends program (ctrl + D) we will get EOFError, in that case go to the next line and quit the program
    except EOFError:
        print()
        break
    #if we have any inappropriate input, just ignore that and repromt the user(just pass)
    except:
        pass
    #if try was succesful without any exceptions we will get to this line of the loop and print total sum
    else:
        print(f'Total: ${total:.2f}')
