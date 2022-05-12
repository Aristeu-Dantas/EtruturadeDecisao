#18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 

#RECEBENDO AS DATAS
dia=int(input('Informe o dia: '))
mes=int(input('Informe o mês: '))
ano=int(input('Informe o ano: '))

#DETERMINANDO AS CONDIÇÕES PARA AS DATAS REFERIDAS
if dia<=0 or dia>31:
    print('Data não confere.')
elif mes<=0 or mes>12:
    print('Data não confere.')

#CONDIÇÕES DO CALENDÁRIO
if mes==1:
    dia>=1 or dia<=31
    print('Data válida!')
elif mes==2:
    dia>=1 or dia<=29
    print('Data válida!')
elif mes==3:
    dia>=1 or dia<=31
    print('Data válida!')
elif mes==4:
    dia>=1 or dia<=30
    print('Data válida!')
elif mes==5:
    dia>=1 or dia<=31
    print('Data válida!')
elif mes==6:
    dia>=1 or dia<=30
    print('Data válida!')
elif mes==7:
    dia>=1 or dia<=31
    print('Data válida!')
elif mes==8:
    dia>=1 or dia<=31
    print('Data válida!')
elif mes==9:
    dia>=1 or dia<=30
    print('Data válida!')
elif mes==10:
    dia>=1 or dia<=31
    print('Data válida!')
elif mes==11:
    dia>=1 or dia<=30
    print('Data válida!')
elif mes==12:
    dia>=1 or dia<=31
    print('Data válida!')
else:
    print('Data não confere')