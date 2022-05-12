#06 - Faça um Programa que leia três números e mostre o maior deles. 

#RECEBENDO OS VALORES
valor1=float(input('Informe um valor: '))
valor2=float(input('Informe outro valor: '))
valor3=float(input('Informe outro valor: '))

#CALCULANDO O MAIOR
if valor1>valor2 and valor1>valor3:
    print('O maior valor informado foi {0}'.format(valor1))
elif valor2>valor1 and valor2>valor3:
    print('O maior valor informado foi {0}'.format(valor2))
elif valor3>valor2 and valor3>valor1:
    print('O maior valor informado foi {0}'.format(valor3))