first = input ('First number: ')
float(first) or int(first)
second = input ('Second number: ')
float(second) or int(second)

choice = input('would you like to + - x or / these numbers?: ')
if choice == '+':
     print (f'sum: {float(first) + float(second)}')
elif choice == '/':
     print (f'sum: {float(first) / float(second)}')
elif choice == 'x':
    print (f'sum: {float(first) * float(second)}')
elif choice == '-':
    print (f'sum: {float(first) - float(second)}')

else:
    print('Thats not a function')