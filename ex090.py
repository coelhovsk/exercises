while True:
    nome = str(input('Nome do aluno: ')).strip().capitalize()
    media = float(input(f'Média de {nome}(0-10): '))
    if media > 10 or media < 0:
        print('Não aceitamos números abaixo de 0 ou acima de 10!!!')
        break
    situacao = ''
    if media < 5:
        situacao = 'Reprovado'
    elif 5 <= media < 6:
        situacao = 'Recuperação'
    elif media >= 6:
        situacao = 'Aprovado'

    aluno = {'Nome': nome, 'Media': media, 'Situação': situacao}

    for k, v in aluno.items():
        print(f'{k}: {v}')
    break
