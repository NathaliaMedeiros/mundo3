"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os numa lista.
Caso o valor já exista lá dentro ele NÃO será adicionado.
No final, será exibido todos os valores digitados, em ordem crescente
"""

lst = list()
aux = 0
continua = 's'
i = 0

while continua != 'n':
    aux = (int(input('Digite um valor: ')))
    if aux in lst:
        print('Esse valor já existe na lista')
        continue
    else:
        lst.append(aux)
        print('Valor adicionado com sucesso!')
        continua = input('Deseja continuar? ')
        if continua == 'n':
            break
    i += 1


lst.sort()
print(lst)
