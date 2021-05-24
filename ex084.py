principal = [[], []]
cont = 1
maiorpessoa = menorpessoa = maior = menor = 0

while True:
    pessoanome = [str(input(f'{cont}° Digite Seu Nome: ')).strip().capitalize()]
    pessoapeso = [float(input(f'{cont}° Digite Seu peso: '))]
    principal[0].append(pessoanome[:])
    principal[1].append(pessoapeso[:])

    sn = str(input('Quer Continuar? [S/N] ')).strip().upper()
    if sn not in 'SN':
        print('Unknown Command. Try Again Please.')
        break
    if sn == 'N':
        break

    cont += 1

for m in range(len(principal[1])):

    # ##### #
    # MAIOR #
    # ##### #

    if maior == 0:
        maior = principal[1][m]
    else:
        if maior < principal[1][m]:
            maior = principal[1][m]

        # ##### #
        # MENOR #
        # ##### #

    if menor == 0:
        menor = principal[1][m]

    else:
        if menor > principal[1][m]:
            menor = principal[1][m]

                # ######### #
                # Resultado #
                # ######### #

print(50 * '=')
print(f'Ao todo, você cadastrou {len(principal[0])} pessoas.\n'
      f'O maior peso foi de {maior}Kg. Peso de', end='')
for c in range(len(principal[1])):
    if principal[1][c] == maior:
        print(principal[0][c], end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for c in range(len(principal[1])):
    if principal[1][c] == menor:
        print(principal[0][c], end='')
