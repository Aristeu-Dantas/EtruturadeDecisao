#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#
#                          Até 5 Kg           Acima de 5 Kg
#    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#
#    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
#  receberá ainda um desconto de 10% sobre este total.
#  Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
#  adquiridas e escreva o valor a ser pago pelo cliente. 

#RECEBENDO DADOS
morango=float(input('Informe a quantidade de morangos adquirida em Kgs: '))
maças=float(input('Informe a quantidade de maças adquirida em Kgs: '))

#CALCULANDO
if morango<=5:
    peso_m1=2.5*morango
if morango>5:
    peso_m1=2.2*morango
print('O morango ficou por {:.2f} reais'.format(peso_m1))

if maças<=5:
    peso_m2=2.5*maças
if maças>5:
    peso_m2=2.2*maças
print('As maçãs ficaram por {:.2f} reais'.format(peso_m2))

total=peso_m1+peso_m2
if total>25:
    desconto=total*0.1
    total-=desconto
    print('O total com desconto foi {:.2f} reais.'.format(total))
else:
    print('O total foi {:.2f} reais.'.format(total))