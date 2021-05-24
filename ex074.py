from random import randint
numeros = randint(1, 10), randint(1, 10), randint(1, 10), \
          randint(1, 10), randint(1, 10)
print('os valores sorteados foram:', end=' ')
for n in numeros:
    print(n, end=' ')
# print(f'\nO maior valor sorteado foi {sorted(nome)[-1]}')
# print(f'O menor valor sorteado foi {sorted(nome)[0]}')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
