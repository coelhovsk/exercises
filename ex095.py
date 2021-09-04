dados_jogador = dict()
database = list()

while True:
    dados_jogador["nome"] = str(input('Nome do jogador: '))
    dados_jogador["partidas"] = int(input(f'Quantos jogos {dados_jogador["nome"]} jogou?'))
    lgols = list()

    for ingols in range(dados_jogador["partidas"]):
        lgols.append(int(input(f'   => Quantos gols {dados_jogador["nome"]} fez na partida {ingols}?')))
    dados_jogador["gols"] = lgols[:]
    dados_jogador["total de gols"] = sum(lgols)
    database.append(dados_jogador.copy())

    ask = str(input('Você deseja continuar? [S/N]')).upper().strip()
    while ask[0] not in 'SN':
        print('Por favor digite apenas S para sim ou N para não. ')
        ask = str(input('Você deseja continuar? [S/N]')).upper().strip()
    if ask[0] == 'N':
        break

#    ____        _     _____       _     #
#   / __ \      | |   |  __ \     | |    #
#  | |  | |_   _| |_  | |__) |   _| |_   #
#  | |  | | | | | __| |  ___/ | | | __|  #
#  | |__| | |_| | |_  | |   | |_| | |_   #
#   \____/ \__,_|\__| |_|    \__,_|\__|  #

print(15*'-=-')
print('cod        nome        gols        total')
print(15*'-=-')
for c in range(len(database)):
    for k, v in database[c].items():
        print(f'{c}    {database[c]["nome"]:>11}    {database[c]["gols"]}{database[c]["total de gols"]:>7}')
        break

while True:
    lev = int(input('Deseja ver os dados de qual jogador? "cod"(-1 para parar): '))
    if lev == -1:
        break
    while lev > len(database) - 1:
        print(f'\033[31mNão existe jogador {lev}.\033[m')
        lev = int(input('Deseja ver os dados de qual jogador? "cod"(-1 para parar): '))
    print(15*'-=')
    print(f'Levantamento do jogador {database[lev]["nome"]}.')
    for i, v in enumerate(database[lev]["gols"]):
        print(f'    => Na partida {i}, {database[lev]["nome"]} fez {database[lev]["gols"][i]} gols.')
    print(f'Foi um total de {database[lev]["total de gols"]} gols.')
    print(15*'-=')
print('> > > PROGRAMA ENCERRADO < < <')
