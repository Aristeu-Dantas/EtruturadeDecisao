#17-Faça um Programa que peça um número correspondente a um determinado ano e em seguida 
# informe se este ano é ou não bissexto. 

#RECEBENDO O ANO
ano=int(input('Informe o ano desejado: '))

#DETERMINANDO O ANO BISSEXTO
if ano%4==0:
    if ano%100!=0:
        print('O ano informado é bissexto.')
    else:
        print('O ano informado não é bissexto.')
else:
    print('O ano informado não é bissexto.')