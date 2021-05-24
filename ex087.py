matriz = [[], [], [], [], [], []]
somadospares = somadacolunatres = maior = 0
for linha in range(3):
    for coluna in range(3):
        valor = int(input(f'Digite um número para [l-{linha}, c-{coluna}]'))
        matriz[linha].append(valor)
        if valor % 2 == 0:
            somadospares += valor
            matriz[3] = somadospares
        if coluna == 2:
            somadacolunatres += valor
            matriz[4] = somadacolunatres
        if linha == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
                matriz[5] = maior

print(20*'\n')
print(17*'=')
for c in range(0, 3):
    for aux in range(0, 3):
        print(f'[ {matriz[c][aux]} ]', end=' ')
    print()
print(17*'=')
print(f'A soma dos valores pares é: {matriz[3]}')
print(f'A soma dos valores da coluna tres é: {matriz[4]}')
print(f'O maior valor da linha 2 é: {matriz[5]}')
