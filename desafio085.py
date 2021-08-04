"""
Crie um programa onde o usuário possa digitar sete valores numéricos. Cadastre os numa lista única que mantenha
separado os valores pares e ímpares.
No fim, mostre os valores pares e impares em ordem crescente.
"""

num = [[], []]

for i in range(1, 8):
    x = int(input(f'Digite o {i}º número: '))
    if x % 2 == 0:
        num[0].append(x)
    else:
        num[1].append(x)


num[0].sort()
num[1].sort()
print('=-' * 30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')