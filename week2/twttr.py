text = input('Input: ')

print('Output: ', end='')
for c in text:
    if c in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        continue
    print(c, end='')
print()
