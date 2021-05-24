from random import randint

print('=-' * 15)
print('VAMOS JOGAR ÍMPAR OU PAR')
print('=-' * 15)
player = 0
wins = 0
while True:
    player = int(input('Digite um valor : '))
    computer = randint(0, 10)
    ip = ''
    ip = str(input('IMPAR ou PAR? [I/P]')).strip().upper()
    soma = player + computer
    total = soma % 2
    while ip not in 'IP':
        ip = str(input('IMPAR ou PAR? [I/P]')).strip().upper()
    if ip == 'I':
        if total == 1:
            print(f'A máquina escolheu {computer}, e você escolheu {player}. A soma é {soma}, ímpar.')
            print('VOCÊ VENCEU !!!')
            wins += 1
        if total == 0:
            print(f'A máquina escolheu {computer}, e você escolheu {player}. A soma é {soma}, par.')
            print('Você perdeu.')
            break
    if ip == 'P':
        if total == 0:
            print(f'A máquina escolheu {computer}, e você escolheu {player}. o total é {soma}, par.')
            print('VOCÊ GANHOU !!!')
            wins += 1
        if total == 1:
            print(f'A máquina escolheu {computer}, e você escolheu {player}. o total é {soma}, ímpar.')
            print('Você perdeu.')
            break
print('=-' * 15)
print('-===GAME-OVER===-')
print('=-' * 15)
print(f'Você ganhou {wins} vezes. Tente novamente.')
