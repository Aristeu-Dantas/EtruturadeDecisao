#09 - Faça um Programa que leia três números e mostre-os em ordem decrescente. 

#RECEBENDO OS NUMEROS
n1=float(input('Informe um numero: '))
n2=float(input('Informe outro numero: '))
n3=float(input('Informe outro numero: '))

#CALCULO DA ORDEM DECRESCENTE
if n1>n2>n3:
    print('A ordem decrescente será {0}, {1}, {2}'.format(n1,n2,n3))
elif n1>n3>n2:
    print('A ordem decrescente será {0}, {1}, {2}'.format(n1,n3,n2))
elif n2>n3>n1:
    print('A ordem decrescente será {0}, {1}, {2}'.format(n2,n3,n1))
elif n2>n1>n3:
    print('A ordem decrescente será {0}, {1}, {2}'.format(n2,n1,n3))
elif n3>n1>n2:
    print('A ordem decrescente será {0}, {1}, {2}'.format(n3,n1,n2))
elif n3>n2>n1:
    print('A ordem decrescente será {0}, {1}, {2}'.format(n3,n2,n1))