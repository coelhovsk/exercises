import datetime

cadastro = {"Nome": str(input('Digite seu nome: ')),
            "Idade": datetime.date.today().year - int(input('Ano de nascimento? ')),
            "CTPS": int(input('Carteira de trabalho (0 não tem): '))}

if cadastro["CTPS"] > 0:
    ano_contratacao = int(input('Ano de contratação: '))
    cadastro["Contratacao"] = ano_contratacao
    cadastro["Salario"] = float(input('Salário R$:'))
    cadastro["Aposentadoria"] = ano_contratacao + 45 - datetime.date.today().year + cadastro["Idade"]

print(37*'=')
for k, v in cadastro.items():
    print('   -', k, 'tem o valor: ', v)
print(37*'=')
