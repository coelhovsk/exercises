valores = [], []

for c in range(7):
    val = int(input(f'Digite o {c+1}°. valor: '))
    if val % 2 == 0:
        valores[0].append(val)
    else:
        valores[1].append(val)

print(30*'=')
print(f'Os valores pares foram: {sorted(valores[0])}')
print(f'Os valores ímpares foram: {sorted(valores[1])}')
