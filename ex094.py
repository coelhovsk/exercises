cadastro = dict()
database = list()
while True:
    cadastro["Nome"] = str(input('Nome: ')).capitalize()

    cadastro["Sexo"] = str(input('Sexo: [M/F]')).upper()
    if cadastro["Sexo"] not in 'MF':
        while True:
            print('\033[31mERRO! Por favor digite novamente dentro dos padrões especificados [M/F]\033[m')
            cadastro["Sexo"] = str(input('Sexo: [M/F]')).upper()
            if cadastro["Sexo"] in 'MF':
                break

    cadastro["Idade"] = int(input('Idade: '))

    database.append(cadastro.copy())

    pergunta_continuar = str(input('Você deseja cadastrar mais uma pessoa? [S/N] ')).upper()

    if pergunta_continuar not in 'SN':
        while True:
            print('\033[31mERRO! Por favor digite novamente. Somente [S/N]\033[m')
            pergunta_continuar = str(input('Você deseja cadastrar mais uma pessoa? [S/N] ')).upper()
            if pergunta_continuar == 'S':
                break
            elif pergunta_continuar == 'N':
                break

    if pergunta_continuar == 'N':
        break

idade = 0
media_de_idade = 0
lista_de_mulheres = list()

for contador in range(len(database)):
    idade += database[contador]["Idade"]
    media_de_idade = idade / len(database)
    acima_da_media = list()
    for laco_acima_media in range(len(database)):
        if database[laco_acima_media]["Idade"] > media_de_idade:
            acima_da_media.append(database[laco_acima_media].copy())
    if database[contador]["Sexo"] == 'F':
        lista_de_mulheres.append(database[contador].copy())

print(30*'\033[33m-=')
print(f'Ao todo temos {len(database)} pessoas cadastradas.')
print('Lista de mulheres cadastradas: ')
for contador in range(len(lista_de_mulheres)):
    for k, v in lista_de_mulheres[contador].items():
        print(f'    {k} === {v}', end=' ')
    print()
print(f'A média de idade é {media_de_idade}')
print(f'lista de pessoas acima da media de idade: ')
for contador in range(len(acima_da_media)):
    for k, v in acima_da_media[contador].items():
        print(f'    {k}, === {v} ', end=' ')
    print()
print(30*'-=')
