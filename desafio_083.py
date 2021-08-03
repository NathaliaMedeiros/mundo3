"""
Crie um programa onde o usuário digite uma emxpressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem certa
"""


expressao = list()
ordemParenteses = list()
count = 0
esquerda = 0
direita = 0


expressao = input('Digite a expressão: ')

for i in expressao:
    if i == '(':
        esquerda += 1
        ordemParenteses.append('(')
    if i == ')':
        direita += 1
        ordemParenteses.append(')')


for i in ordemParenteses:
    for j in expressao:
        count += 1
        if i == esquerda:
            #print('Expressão válida!')
            break
        else:
            print('Sua expressão está errada')


"""
if direita == esquerda:
    print('Expressão válida!')
else:
    print('Sua expressão está errada')

"""

