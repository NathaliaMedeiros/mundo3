"""
Crie um programa que vai ler varios numeros e colocar numa lista. Depois disso, mostre:
A- Quantos números foram digitados
B- A lista de valores ordenada de forma decrescente
C- Se o valor 5 foi ou não digitado na lista
"""

lst = list()
continuar = 's'
contador = 0


while continuar != 'n':
    lst.append(int(input('Digite um valor: ')))
    contador += 1
    continuar = input('deseja continuar? ')

lst.sort(reverse=True)

print(f'Você digitou {contador} elementos')
print(f'Lista de valores em ordem decrescente: {lst}')

if 5 in lst:
    print("O valor 5 faz parte da lista!")
else:
    print('O valor 5 não faz parte da lista')

