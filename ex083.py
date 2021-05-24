expr = str(input('Digite Sua Expressão: '))
pilha = []

for simbolo in expr:
    print(pilha)
    if simbolo == '(':
        pilha.append('(')

    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(')')
            break

print(pilha)
if len(pilha) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')
