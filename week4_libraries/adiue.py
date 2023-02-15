import sys

#empty list for names
names = []

#ask user for names untill ctrl+d typed
while True:
    try:
        name = input('Name: ')
        #add names to list
        names.append(name)
    #if user types ctrl+d go one line down and stop asking for names
    except EOFError:
        print()
        break
#index for names list
index = 0

#beginning of output
print("Adieu, adieu, to ", end='')

#1 and 2 names have slightly different printing format
if len(names) == 1:
    print(names[0])
    sys.exit()
elif len(names) == 2:
    print(f"{names[0]} and {names[1]}")
    sys.exit()

#for 3 and more names
while len(names) - 1 > index:
    print(f'{names[index]}, ', end='')
    index += 1
#end of output for 3 and more names,  after  1 and 2 program was terminated
print(f'and {names[index]}')
