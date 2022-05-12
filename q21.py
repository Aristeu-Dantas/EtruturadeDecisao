#21 - Faça um Programa para um caixa eletrônico. 
#O programa deverá perguntar ao usuário a valor do saque e depois informar quantas 
#notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
#O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a 
#quantidade de notas existentes na máquina.

#    a-Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
#  uma nota de 50, uma nota de 5 e uma nota de 1;
#    b-Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. 

#RECEBENDO O VALOR DO SAQUE
saque=int(input('Informe o valor que quer sacar: '))

#CONSTRUTORES
total=saque
ced=100
totalced=0

#CALCULANDO
if saque<10 or saque>600:
    print('Limite de saque: 10,00 à 600,00 reais.')
else: 
    print('Verificando notas ...')
while True:
    if total>=ced:
        total-=ced
        totalced+=1
    else:
        if totalced>0:
            print('O total de {0} cédulas de R${1}'.format(totalced,ced))
        if ced==100:
            ced=50
        elif ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=5
        elif ced==5:
            ced=1
        totalced=0
        if total==0:
            break
