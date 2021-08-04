"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No fim, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves
"""

pessoas = list()
nome_peso = list()
menor = maior = 0


while True:
    pessoas.append(input('Nome: '))
    pessoas.append(int(input('Peso: ')))

    if len(nome_peso) == 0:
        menor = pessoas[1]
        maior = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    nome_peso.append(pessoas[:])
    pessoas.clear()
    continuar = input('Deseja continuar? ')
    if continuar in 'Nn':
        break


nome_peso.sort()

print(f'Ao todo você cadastrou {len(nome_peso)} pessoas.')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for n in nome_peso:
    if n[1] == maior:
        print(f'[{n[0]}] ', end='')

print()
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for n in nome_peso:
    if n[1] == menor:
        print(f'[{n[0]}] ', end='')


