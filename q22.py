#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão).

#RECEBENDO NUMERO
numero=int(input('Informe um numero inteiro: '))

#CALCULANDO
if numero%2:
    print('O numero informado é ímpar.')
else:
    print('O numero informado é par.')