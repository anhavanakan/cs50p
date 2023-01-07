camel = input('camelCase: ').strip()
print('snake_case: ', end='')
for c in camel:
    if c.isupper():
        print('_', end='')
        print(c.lower(), end='')
        continue
    print(c, end='')
