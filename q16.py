#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
#O programa deverá pedir os valores de a, b e c e fazer as consistências, 
#informando ao usuário nas seguintes situações:
#
#  a-Se o usuário informar o valor de A igual a zero, 
#a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#  b-Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#  c-Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#  d-Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

a=int(input('Informa o valor de "a": '))
if a==0:
    print('O programa foi encerrado.')
else:
    b=int(input('Informa o valor de "b": '))
    c=int(input('Informa o valor de "c": '))
    delta=b*b+(4*a*c)
    if delta<0:
        print('Delta menor que 0. Raízes imaginárias. Tchau')
    elif delta==0:
        raiz = -b / (2*a)
        print('Delta=0 , raiz = ',raiz)
    else:
        raiz1 = (-b + math.sqrt(delta) ) / (2*a)
        raiz2 = (-b - math.sqrt(delta) ) / (2*a)
        print('Raizes: ',raiz1,' e ',raiz2)