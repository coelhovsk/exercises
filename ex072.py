numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
extenso = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
           'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
opcao = int(input('Escolha um número entre 1 e 20: '))
while opcao not in numeros:
    opcao = int(input('Ocorreu algum erro. Tente Novamente. Escolha um número entre 1 e 20: '))
print(f'Você digitou o número {extenso[opcao-1]}')
