"""
Faça um programa que leia 5 valores numericos e guarde numa lista.
No final, mostre qual foi o maior e o menor e suas respectivas posições na lista
"""

lst = list()
maiorValor = 0
menorValor = 0
menorPosicao = 0
maiorPosicao = 0

for i in range(0, 5, 1):
    lst.append(int(input(f'Digite o valor {i}: ')))
    if i == 0:
        menorValor = lst[i]
        maiorValor = lst[i]
    else:
        if lst[i] <= menorValor:
            menorValor = lst[i]
            menorPosicao = i
        elif lst[i] >= maiorValor:
            maiorValor = lst[i]
            maiorPosicao = i


print(f'Você digitou os valores: {lst}')
print(f'O menor valor digitado foi {menorValor} na posição {menorPosicao}')
print(f'O maior valor digitado foi {maiorValor} na posição {maiorPosicao}')
