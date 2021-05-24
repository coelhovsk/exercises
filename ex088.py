import random
import time
aleatory_numbers_list = list()
logo = 'JOGA NA MEGA SENA'

print('-'*30)
print(f'{logo:^30}')
print('-'*30)

quantidade_de_jogos_sorteados = int(input('Quantos jogos vai querer? '))

print(f'-=-=-=     Sorteando {quantidade_de_jogos_sorteados} jogos...      =-=-=-')

for jogo in range(0, 1*quantidade_de_jogos_sorteados):
    for c in range(0, 6):
        aleatory_number = str(random.randint(1, 60))
        aleatory_numbers_list.append(aleatory_number[:])
    print(f'Jogo {jogo+1}:', end=' ')
    print(aleatory_numbers_list[0:6])
    aleatory_numbers_list.clear()
    time.sleep(1)
