pa = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
cont = 0
a = 10
op = -1
while op != 0:
    print()

    while cont < 10:
        print(pa, end=' - ')
        pa += razao
        cont += 1
    print('PAUSE')

    op = int(input('Quantos quer a mais ? '))
    a += op

    if op > 0:
        while cont < a:
            print(pa, end=' - ')
            pa += razao
            cont += 1
        print('PAUSE')

print('Fim!')
