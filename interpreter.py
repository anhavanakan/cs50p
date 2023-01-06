expression = input('Expression: ').strip()
x, y, z = expression.split()
x = float(x)
z = float(z)
if y == '+':
    print(x+z)
elif y == '-':
    print(x-z)
elif y == '*':
    print(x*z)
elif y == '/' and z != 0:
    print(round(x/z, 1))
