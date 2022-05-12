#Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
#  Dica: utilize uma função de arredondamento. 

#RECEBENDO E TRANSFORMANDO EM STRING
numero=float(input('Informe um numero inteiro ou decimal: '))
numero=str(numero)

if numero[:1]==0:
    print('O numero informado é inteiro.')
else:
    print('O numero informado é decimal.')