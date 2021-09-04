from random import randint
from time import sleep
sorteio_lista = list()


def sorteio():
    for c in range(5):
        sorteio_lista.append(randint(0, 30))
    print('Sorteando 5 valores: ', end='')
    for i, v in enumerate(sorteio_lista):
        print(v, end=' ')
        sleep(0.4)
    print('PRONTO!')


def soma_dos_pares():
    soma_inteira = 0
    for i, v in enumerate(sorteio_lista):
        if v % 2 == 0:
            soma_inteira += v
    print(f'A soma dos números pares de {sorteio_lista} é: {soma_inteira}')


sorteio()
soma_dos_pares()
