cont = 0
atual = 1
anterior = 0
aux = 0
mais = -1
mais1 = int(input('Quantos vc quer? '))

while mais != 0:
    while cont < mais1:
        print(atual, end=' - ')

        aux = atual
        atual += anterior
        anterior = aux

        cont += 1
        if cont == mais1:
            mais1 = int(input('Quanto quer a mais? '))
            mais1 += cont
