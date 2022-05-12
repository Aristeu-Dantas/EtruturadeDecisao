#08 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#  sabendo que a decisão é sempre pelo mais barato. 

#RECEBENDO OS VALORES
valor1=float(input('Informe o valor do primeiro produto: '))
valor2=float(input('Informe o valor do segundo produto: '))
valor3=float(input('Informe o valor do terceiro produto: '))

#CALCULANDO O MELHOR PRODUTO
if valor1<valor2 and valor1<valor3:
    print('O melhor produto é o que custa {0} reais'.format(valor1))
elif valor2<valor1 and valor2<valor3:
    print('O melhor produto é o que custa {0} reais'.format(valor2))
elif valor3<valor2 and valor3<valor1:
    print('O melhor produto é o que custa {0} reais'.format(valor3))