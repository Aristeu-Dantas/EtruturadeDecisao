#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#    a-par ou ímpar;
#    b-positivo ou negativo;
#    c-inteiro ou decimal. 

#RECEBENDO INFOS
numero1=float(input('Informe o primeiro numero: '))
numero2=float(input('Informe o segundo numero: '))
operaçao=str(input('Qual a operação você deseja fazer? ')).upper()

#CALCULADORA
if operaçao=='ADIÇÃO' or operaçao=='SOMA':
    operaçao=numero1+numero2
    print('O resultado é {0}'.format(operaçao))
elif operaçao=='SUBTRAÇÃO' or operaçao=='DIMINUIR':
    operaçao=numero1-numero2
    print('O resultado é {0}'.format(operaçao))
elif operaçao=='DIVISÃO' or operaçao=='DIVIDIR':
    operaçao=numero1/numero2
    print('O resultado é {0}'.format(operaçao))
elif operaçao=='MULTIPLICAÇÃO' or operaçao=='MULTIPLICAR':
    operaçao=numero1*numero2
    print('O resultado é {0}'.format(operaçao))
else:
    print('Informe apenas uma das 4 operações básicas.')

#ÍMPAR OU PAR
if operaçao%2:
    print('O resultado é ímpar.')
else:
    print('O resultado é par.')

#POSITIVO OU NEGATIVO
if operaçao>0:
    print('O resultado é positivo.')
elif operaçao<0:
    print('O resultado é negativo.')
else:
    print('O resultado é zero.')

#INTEIRO OU DECIMAL
if operaçao%1==0:
    print('O numero informado é inteiro.')
else:
    print('O numero informado é decimal.')