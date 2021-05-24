values = list()

print('\033[32m=-\033[m' * 30)

while True:

    add = int(input('Insert value: '))

    while True:

        if add in values:
            print('\033[31m!!!', '=-' * 20, '!!!\033[m')
            print("Duplicated Value! I Don'T Add...")
            print('\033[31m!!!', '=-' * 20, '!!!\033[m')
            break

        if add not in values:
            values.append(add)
            print('Value Added Successfully!')
            break

    sn = str(input('Do you want continue? [Y/N]')).upper().strip()

    while sn not in 'YSN':
        print('\033[31mUnknown option.\033[m')
        sn = str(input('Do you want continue? [Y/N]')).upper().strip()

    if sn in 'NO':
        break

print('\033[32m=-\033[m' * 30)
print(f'\033[33mYou entered values\033[m \033[36m {sorted(values)}')
print('\033[32m=-\033[m' * 30)
