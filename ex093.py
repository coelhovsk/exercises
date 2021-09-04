dados_jogador = dict()
total = 0
dados_jogador["nome"] = str(input('Nome do jogador: '))
dados_jogador["partidas"] = int(input(f'Quantos jogos {dados_jogador["nome"]} jogou?'))
lgols = list()

print(dados_jogador)

for ingols in range(dados_jogador["partidas"]):
    lgols.append(int(input(f'Quantos gols {dados_jogador["nome"]} fez na partida {ingols}?')))
dados_jogador["gols"] = lgols[:]
dados_jogador["total de gols"] = sum(lgols)

print(15*'\033[33m-=')
for k, v in dados_jogador.items():
    print(f'o campo {k} tem o valor de {v}')
print(15*'-=')

print(f'O jogador {dados_jogador["nome"]} jogou {dados_jogador["partidas"]} partidas.')

for i, v in enumerate(lgols):
    print(f'    => Na partida {i}, {dados_jogador["nome"]} fez {v} gols.')
print(f'Foi um total de {dados_jogador["total de gols"]} gols.')
print(15*'-=')
print('\033[m')
