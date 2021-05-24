values = list()

# Ler valores

while True:
    add = int(input('Digite um valor: '))
    values.append(add)
    sn = str(input('Quer continuar? [S/N]')).strip().upper()
    while sn not in 'SN':
        print('\033[31mUnknown option.\033[m')
        print('Tente novamente.')
        sn = str(input('Quer continuar? [S/N]')).strip().upper()
    if sn == 'N':
        break
# Mostrar os valores em uma lista
values.sort()
print(f'A lista em forma crescente é: {values}')

# Mostrar os pares em forma crescente

pares = list()
for i, v in enumerate(values):
    if v % 2 == 0:
        pares.append(v)
pares.sort()
print(f'A lista em forma crescente somente com números pares: {pares}')

# Mostrar
naopares = list()
for i, v in enumerate(values):
    if v % 2 == 1:
        naopares.append(v)
print(f'A lista em forma crescente somente com números ímpares: {naopares}')
