#01 - Faça um Programa que peça dois números e imprima o maior deles. 

#pedindo os números

n1=int(input('Informe um numero: '))
n2=int(input('Informe outro numero: '))

#distinguindo o maior

if n1>n2:
    print('O maior numero é o {0}'.format(n1))
else:
    print('O maior numero é o {0}'.format(n2))