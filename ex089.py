import time
main = [[], [], [], []]
cont = 0
continuar = ''

while True:
    main[0].append(str(input('Nome: ')).strip())
    main[1].append(float(input('Nota 1: ')))
    main[2].append(float(input('Nota 2: ')))
    media = (main[1][cont] + main[2][cont]) / 2
    main[3].append(media)

    cont += 1

    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar not in 'SN':
        while continuar not in 'SN':
            print('\033[1;31mResposta inválida.\033[m')
            continuar = str(input('Quer continuar? [S/N]')).upper().strip()
            if continuar == 'N':
                break
            elif continuar == 'S':
                break
    if continuar == 'N':
        break

print(10*'\033[1;33m-=-')
print('N°  ---   Aluno   ---  Média')
print(10*'-=-')
for indice in range(len(main[0])):
    print(f'{indice:<6}    {main[0][indice]:^8}    {main[3][indice]:>6.2f}')
print(10*'-=-')

while True:
    mostrar_nota_do_aluno = int(input('\033[mMostrar a nota do aluno ( número do aluno )[999 para interromper]: '))
    if mostrar_nota_do_aluno == 999:
        break
    elif mostrar_nota_do_aluno >= len(main[0]):
        print('\033[1;31mResposta inválida. Tente Novamente.\033[m')
    elif mostrar_nota_do_aluno <= len(main[0]):
        print(f'\033[1;32mNotas de {main[0][mostrar_nota_do_aluno]} são ({main[1][mostrar_nota_do_aluno]:.2f}, {main[2][mostrar_nota_do_aluno]:.2f})')

print(10*'-=-')
print('\033[1;33mFinalizando...')
time.sleep(1)
print('\033[1;32m<<< Volte sempre! >>>\033[m')
