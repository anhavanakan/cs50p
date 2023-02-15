from sys import argv, exit

if len(argv) == 1:
    exit("Specify filename")
elif len(argv) > 2:
    exit("Too many arguments")
elif not ".py" in argv[1]:
    exit("Specify python file")

try:
    file = open(argv[1])
except FileNotFoundError:
    exit("There is no such file")

lines = file.readlines()
count = 0
for line in lines:
    #comments where before '#' could be whitespaces
    if line.lstrip().startswith('#'):
        continue
    #if line has whitespaces it will be striped and '\n' will remain
    if line.strip(' ')== '\n':
        continue
    #if its a last line, only with whitespaces and without '\n'
    if line.strip(' ') == '':
        continue
    count += 1

print(count)

file.close()
