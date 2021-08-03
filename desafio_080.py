"""
Crie um programa onde o usuario possa digitar 5 valores numericos e cadastre-os numa lista, já na posição correta
de inserção (sem usar o sort).
No final, mostre a lista ordenada
"""

i = 0
lst = list()


for i in range(0, 5, 1):
    lst.append(int(input('Insira um valor: ')))
    if i == 0:
        print('Valor adicionado ao início da lista')
    elif i == 1 and lst[i] < lst[i - 1] :
        print('Valor adicionado a posição 0 da lista')
    elif lst[i] >= lst[i - 1]:
        print('Valor adicionado ao fim da lista')
    else:
        while lst[i] < lst[i - 1]:
            i -= 1
        lst.append()

print(lst)

"""
lst = list()
aux = 0


for i in range(0, 5, 1):
    lst.append(int(input(f"Digite o valor {i}: ")))
    if i == 0:
        continue
    elif lst < lst[i - 1]
print(lst)

"""