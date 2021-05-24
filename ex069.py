idade = sexo = 0
qsexom = qidademenorm = qsexof = qidademenorf = qidademaiorf = qidademaiorm = 0
while True:
    # -========== ==========-
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    # -========== Input  ==========-
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    # -========== ==========-
    print('-' * 30)
    opcao = str(input('Quer continuar? [S/N]')).strip().upper()
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()
    # -========== Condições ==========-
    if idade >= 18:
        if sexo == 'M':
            qsexom += 1
            qidademaiorm += 1
        if sexo == 'F':
            qsexof += 1
            qidademaiorf += 1
    if idade < 18:
        if sexo == 'M':
            qsexom += 1
            qidademenorm += 1
        if sexo == 'F':
            qsexof += 1
            qidademenorf += 1
    # -========== Prints ==========-
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {qidademaiorf + qidademaiorm}\n'
      f'Total de pessoas com menos de 18 anos: {qidademenorf + qidademenorm}\n'
      f'Total de Homens com mais de 18 anos: {qidademaiorm}\n'
      f'Total de Mulheres com mais de 18 anos: {qidademaiorf}\n'
      f'Total de Homens com menos de 18 anos: {qidademenorm}\n'
      f'Total de Mulheres com menos de 18 anos: {qidademenorf}\n'
      f'Ao todo temos {qsexom} homem(s), e {qsexof} mulher(s).')
#     -========== THE END ===========-
#     -==============================-
