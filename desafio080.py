"""
Crie um programa onde o usuario possa digitar 5 valores numericos e cadastre-os numa lista, já na posição correta
de inserção (sem usar o sort).
No final, mostre a lista ordenada
"""

lst = list()


for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > lst[-1]:
        lst.append(n)
        print('Valor inserido ao final da lista.')
    else:
        pos = 0
        while pos < len(lst):
            if n <= lst[pos]:
                lst.insert(pos, n)
                print(f'Valor inserido na posição {pos}')
                break
            pos += 1

print('-=' * 30)
print(f'Os valores digitados são: {lst}')

