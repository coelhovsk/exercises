from datetime import datetime
from time import sleep
base = dict()
print('-=< 𝒬𝓊𝑒𝓂 𝒫𝑜𝓊𝓅𝒶𝒯𝑒𝓂  >=-')


def menu():
    print('1 - Novo Cliente\n'
          '2 - Debita\n'
          '3 - Deposita\n'
          '4 - Saldo\n'
          '5 - Extrato\n'
          '6 - Apagar Cliente\n')
    print()
    print()
    print('0 - Sair\n'
          ' ')

    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        registro()
    if opcao == 6:
        apagar_cliente()


def buscar_usuario(aux):
    """
    Essa função busca o CPF do usuário em users.txt
    e retorna o valor True se o CPF ja estiver cadastrado.
    """
    with open('users.txt', 'r') as arquivo:
        if aux in arquivo.read():
            """
            Aux é o CPF do usuário. Se o CPF estiver em arquivo(users.txt) 
            mostrar mensagem de erro.
            """
            print(45 * '\033[30m-=')
            print(
                '\033[31mO CPF escrito ja está cadastrado, por favor verifique seu CPF ou selecione outra opção.\033[m')
            print(45 * '\033[30m-=\033[m')

            sleep(1.5)

            menu()
            return True


def registro():
    """
    Essa função vai perguntar o nome do cliente,o cpf do mesmo,
    tipo de conta, valor de entrada e uma senha para o usuário.
    """
    base["nome"] = str(input('Nome: '))

    base["cpf"] = str(input('Informe seu CPF(sem pontuação): '))
    while len(base["cpf"]) != 11:
        print('\033[31mO CPF informado não corresponde o formato correto. Por favor verifique-o\n'
              'Digite sem pontuação.\033[33m Ex: 12345678900\033[m')
        base["cpf"] = str(input('Informe seu CPF(sem pontuação): '))

    print('> > > Tipo de conta < < <')
    print(f'{"Conta Salário[1]":>21}\n{"Conta Corrente[2]":>21}\n{"Plus[3]":>21}')
    base["conta"] = int(input('Digite aqui: '))

    base["saldo"] = float(input('Digite o valor inicial que será depositado:'))

    base["senha"] = input('Digite a senha que será usada: ')

    buscar_usuario(base["cpf"])

    if buscar_usuario:
        with open('users.txt', 'a+', newline='') as arquivo:
            arquivo.writelines(f'{base.items()} {datetime.now()}\n')


def saldo():
    """
    """


def deposito():
    """
    """


def saque():
    """
    """


def extrato():
    """
    """


def apagar_cliente():
    """
    Essa função deleta um usuário a partir do seu CPF e a senha.
    """
    with open('users.txt', 'r') as arquivo:
        data = arquivo.readlines()

    def excluir(nome_arquivo, numero_linha):
        """
        Esse programa recebe 3 parâmetros:
       :'nome_arquivo': Recebe o
        nome do arquivo txt onde esta cadastrado todos os users.
       :'numero_linha': Recebe o número da linha onde o usuário que
        você deseja excluir
        """
        linhas = open(nome_arquivo, 'r').readlines()
        linhas[numero_linha] = ''
        out = open(nome_arquivo, 'w')
        out.writelines(linhas)
        out.close()

    base["cpf"] = str(input('CPF da conta que deseja excluir:'))
    base["senha"] = input('Senha do usuário: ')
    print(base["senha"], base["cpf"])
    for linha in range(len(data)):
        """
        Esse laço descobre a linha onde se localiza o usuário que será excluido.
        """
        if base["cpf"] in data[linha]:
            if base["senha"] not in data[linha]:
                while True:
                    print('='*60)
                    print('A senha não condiz com o CPF, por favor tente novamente.')
                    print('='*60)
                    base["cpf"] = str(input('CPF da conta que deseja excluir:'))
                    base["senha"] = input('Senha do usuário: ')
                    if base["cpf"] and base["senha"] in data[linha]:
                        break
            if base["senha"] in data[linha]:
                excluir('users.txt', linha)


menu()
