cont = 0
valores = int(input('Digite Um Número: ')), int(input('Digite Outro Número: ')),\
          int(input('Digite Mais Um Número: ')), int(input('Digite o Último Número: '))
print(f'Você digitou os valores: {valores}')

# =============================================
for c in valores:
    if c == valores[0]:
        cont += 1
print(f'O primeiro valor {valores[0]}, apareceu {cont} vezes')
print('Os valores pares foram: ', end='')
for c in valores:
    if c % 2 == 0:
        print(c, end=', ')
