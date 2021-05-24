matriz = [[], [], [], []]

for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite um número para [l-{linha}, c-{coluna}]')))
for c in range(0, 3):
    for aux in range(0, 3):
        print(f'[ {matriz[c][aux]} ]', end=' ')
    print()
