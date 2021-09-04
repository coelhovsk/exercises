from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}

for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(.75)


def podio():
    place = 1
    print(4*'=-', 'PODIO', 4*'=-', end='' '=')
    print()
    for key, value in sorted(jogadores.items(), key=itemgetter(1), reverse=True):
        sleep(.75)
        print(f'-= {place}°: {key} with {value} =-')
        place += 1
    print(11*'=-', end='' '=')


podio()
a = 1

