n = soma = cont = 0
while True:
    n = int(input('Digite um número[ou 999 para parar] '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma entre esses {cont} valores é {soma}')
