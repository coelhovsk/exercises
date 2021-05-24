maismil = price = total = cont = maiorpreco = 0
menornome = ''
print('-'*30)
print('      LOJA SUPER BARATÃO')
print('-'*30)
while True:
    product = str(input('Nome do Produto: ')).strip()
    price = float(input('Preço do Produto: R$ '))
    menorpreco = price
    cont += 1
    if price > 1000:
        maismil += 1
    if cont == 1 or price < menorpreco:
        menorpreco = price
        menornome = product
    if price > maiorpreco:
        maiorpreco = price
    total += price
    sn = str(input('Quer continuar? [S/N] ')).strip().upper()
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()
    if sn == 'N':
        break
print(f'O total da compra foi R${total:.2f} \n'
      f'Temos {maismil} produtos custando mais de 1000.00\n'
      f'O produto mais barato foi {menornome} que custa {menorpreco:.2f}')
