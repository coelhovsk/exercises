values = list()

print('\033[32m=-\033[m'*25)

for c in range(0, 5):
    values.append(int(input(f'\033[33m[Pos({c+1})]Digite um valor: \033[m')))


menor = min(values)
maior = max(values)


print('\033[32m=-\033[m'*25)


print('\033[31mVocê digitou os valores \033[m', end='')
for va in values:
    print(va, end=' ')
print()


print('\033[32m=-\033[m'*25)


print(f'\033[34mO menor valor foi {menor} que está nas posições \033[m', end='')
for i, v in enumerate(values):
    if v == menor:
        print(f'{i + 1}', end='...')


print(f'\n\033[34mO maior valor foi {maior} que está nas posições \033[m', end='')
for i, v in enumerate(values):
    if v == maior:
        print(f'{i + 1}', end='...')
print()


print('\033[32m=-\033[m'*25)
