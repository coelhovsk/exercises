pa = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
cont = 0

print()
while cont < 10:
    print(pa, end=' - ')
    pa += razao
    cont += 1

print('Fim!')
