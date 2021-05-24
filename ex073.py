times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminese', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
c = 0

print('=-' * 30)
print('Lista dos times do Brasileirão:', times)
print('=-' * 30)
print('Os 5 primeiros', times[0:5])
print('=-' * 30)
print('Os quatro últimos são:', times[-4:])
print('=-' * 30)
print('Times em ordem alfabetica:', sorted(times))
print('=-' * 30)
for cont in times:
    c += 1
    if cont == 'Chapecoense':
        print(f'Chapecoense está em {c}° lugar.')
        break
