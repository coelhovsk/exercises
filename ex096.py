def area(a, b):
    print(f'A área de um terreno {a}x{b} é igual a {a * b}m².')


print(30*'—')
print(f'{"CONTROLE DE TERRENOS":^30}')
print(30*'—')
largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite o comprimento do terreno (m): '))
area(a=largura, b=comprimento)
