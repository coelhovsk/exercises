from random import randint
from time import sleep


def maior(*numeros):
    print(60 * '—')
    print('Analisando os valores..')
    maiornum = -999999999999
    if len(numeros) != 0:
        for val in numeros:
            if maiornum == -999999999999:
                maiornum = val
            if val > maiornum:
                maiornum = val
        for val in numeros:
            print(val, end=' ')
            sleep(0.35)
        print(f'Foram informados {len(numeros)} valores. {maiornum} é o maior.')
        print(60 * '—')
    if len(numeros) == 0:
        print('Foram informados 0 valores. Não existe maior número.')


maior(randint(0, 30), randint(0, 30), randint(0, 30), randint(0, 30))
maior(randint(0, 30), randint(0, 30), randint(0, 30))
maior(randint(0, 30), randint(0, 30))
maior(randint(0, 30))
maior()
print(60 * '—')
