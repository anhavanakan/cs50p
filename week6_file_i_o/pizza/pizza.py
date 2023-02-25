rom sys import argv, exit
import csv
from tabulate import tabulate

if len(argv) == 1:
    exit("Too few command-line arguments")
elif len(argv) > 2:
    exit("Too many command-line arguments")
elif not ".csv" in argv[1]:
    exit("Not a CSV file")
# there wi will store all our data as list
table = []
try:
    with open(argv[1]) as file:
        # menu is like a file discriptor in C
        menu = csv.reader(file)
        for row in menu:
            # creating list of rows of menu
            table.append(row)
        # if we specify header it will deliminate header row from usual rows
        # grid is for '+' signs where lines(------) are intersect
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    exit("File does not exist")
