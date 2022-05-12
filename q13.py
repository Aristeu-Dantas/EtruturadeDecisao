#13 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 

#RECEBENDO O DIA
dia=int(input('Informe um numero de 1 a 7 que corresponda a um dia da semana: '))

#CALCULANDO
if dia==1:
    print('Domingo')
elif dia==2:
    print('Segunda')
elif dia==3:
    print('Terça')
elif dia==4:
    print('Quarta')
elif dia==5:
    print('Quinta')
elif dia==6:
    print('Sexta')
elif dia==7:
    print('Sábado')
elif dia<1 or dia>7:
    print('Valor inválido')