cont = 0
print('=' * 30)
print('===========Tabuada============')
print('=' * 30)
n = int(input('Digite um valor: '))
print('-' * 30)
while True:
    print(f'{n} x {cont} é = {n * cont}')
    cont += 1
    if cont == 11:
        print('-' * 30)
        cont = 0
        n = int(input('Digite um valor: '))
    if n < 0:
        break
