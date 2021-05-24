values = list()

print('\033[32m=-\033[m' * 30)

for c in range(0, 5):

    number = int(input('Enter a Value: '))

    if c == 0 or number > values[-1]:
        values.append(number)
        print('\033[34mThe value was inserted at the end of the list.\033[m')

    else:

        pos = 0

        while pos != len(values):

            if number <= values[pos]:
                values.insert(pos, number)
                print(f'\033[34mThe value was entered at position \033[34m{pos + 1}\033[m in the list.\033[m')
                break
            pos += 1

print('\033[32m=-\033[m' * 30)
print(f'The values entered: {values}')
print('\033[32m=-\033[m' * 30)
