greeting = input('Say something: ').strip().lower()
if greeting.find('hello') == 0:
    print('$0')
elif greeting.find('h') == 0:
    print('$20')
else:
    print('$100')
