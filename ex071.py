from math import trunc
totcintrunc = totvintetrunc = totdeztrunc = totumtrunc = 0
print('=' * 30)
print('{:^30}'.format('BANCO DO BRASIL'))
print('=' * 30)
while True:
    sacar = float(input('Que valor você quer sacar? R$'))
    while sacar != 0:
        # CINQUENTA
        totcin = sacar / 50
        totcintrunc = trunc(totcin)
        sacar -= totcintrunc * 50
        break
    while sacar != 0:
        # VINTE
        totvinte = sacar / 20
        totvintetrunc = trunc(totvinte)
        sacar -= totvintetrunc * 20
        break
    while sacar != 0:
        # DEZ
        totdez = sacar / 10
        totdeztrunc = trunc(totdez)
        sacar -= totdeztrunc * 10
        break
    while sacar != 0:
        # UM
        totum = sacar / 1
        totumtrunc = trunc(totum)
        sacar -= totumtrunc * 1
        break
    if sacar == 0:
        break
print(f'Total de {totcintrunc} cédulas de R$50\n'
      f'Total de {totvintetrunc} cédulas de R$20\n'
      f'Total de {totdeztrunc} cédulas de R$10\n'
      f'Total de {totumtrunc} moedas de R$1')
