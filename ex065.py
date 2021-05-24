opcao = "s"
n = soma = cont = menor = maior = 0
while opcao in "Ss":
    n = int(input('Digite um valor: '))
    cont += 1
    if cont == 1:
        maior = menor = n
    if menor < n:
        menor = menor
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    soma += n
    media = soma / cont
    opcao = input('Você quer continuar? [S/N]').lower().strip()
print(f'Você digitou {cont} números, A média de tudo é {media}')
print(f'O menor valor foi {menor} e o maior foi {maior}.')
