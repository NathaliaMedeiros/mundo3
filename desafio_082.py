"""
Crie um programa que vai ler vários números e colocar numa lista.
Crie duas listas extras que vão conter apenas os valores pares e os ímpares.
Mostrar o resultado das 3 listas
"""

lst = list()

continuar = 's'

while continuar != 'n':
    lst.append(int(input('Insira um valor: ')))
    continuar = input('Deseja continuar? ')

lstPar = []
lstImpar = []

for i in lst:
    if i % 2 == 0:
        lstPar.append(i)
    else:
        lstImpar.append(i)


print(f'Lista completa é {lst}')
print(f'Lista de pares: {lstPar}')
print(f'Lista de ímpares: {lstImpar}')


