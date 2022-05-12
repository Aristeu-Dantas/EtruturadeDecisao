#02 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

#recebendo o valor

valor=int(input('Informe um valor positivo ou negativo: '))

#Distinguindo o valor

if valor>0:
    print('O valor é positivo.')
elif valor<0:
    print('O valor é negativo.')
else:
    print('O valor é igual a zero.')