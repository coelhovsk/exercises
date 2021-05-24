values = list()

print('\033[32m=-\033[m' * 30)

while True:

    n = int(input('Enter a value: '))
    values.append(n)
    yn = str(input('You want continue? [Y/N]')).strip().upper()

    while yn not in 'YN':

        print('\033[31mUnknown option.\033[m')
        print('Try again.')

        yn = str(input('Do you want continue? [Y/N]')).strip().upper()

    if yn == 'N':
        break

print('\033[32m=-\033[m' * 30)

print(f'You entered {len(values)} elements.')

values.sort(reverse=True)

print(f'Values in descending order: {values}')

if 5 in values:
    print('The value 5 has been entered and is in the list.')
else:
    print('The value 5 has not been entered in the list.')
print('\033[32m=-\033[m' * 30)
