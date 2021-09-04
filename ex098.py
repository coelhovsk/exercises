from time import sleep


def contador(a, b, c):
    print(30 * '—')
    for c in range(a, b, c):
        print(c, end=' ')
        sleep(0.2)
    print()


contador(1, 11, 1)
contador(10, -1, -2)
print(30 * '—')
inicio = int(input('Inicio da sequência: '))
fim = int(input('Fim da sequência: '))
razao = int(input('Razão da sequência: '))
if razao < 0:
    razao = razao * 2
if razao == 0:
    razao = 1
if fim < inicio:
    contador(inicio, fim - 1, razao - razao * 2)
contador(a=inicio, b=fim + 1, c=razao)
