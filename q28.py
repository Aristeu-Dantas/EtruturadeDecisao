#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                          Até 5 Kg           Acima de 5 Kg
#    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg#
#    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
#  porém não há limites para a quantidade de carne por cliente.
#  Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
#  Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
#  contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, 
#  valor do desconto e valor a pagar.

#RECEBENDO DADOS
carne=input('Informe a carne que deseja: ').lower().strip()
kg=float(input('Informe a quantidade em kg que deseja: '))

#CALCULANDO
if carne=='file duplo':
    if kg<=5:
        valor=4.9*kg
    if kg>5:
        valor=5.8*kg
elif carne=='alcatra':
    if kg<=5:
        valor=5.9*kg
    if kg>5:
        valor=6.8*kg
elif carne=='picanha':
    if kg<=5:
        valor=6.9*kg
    if kg>5:
        valor=7.8*kg
else:
    print('Carne não encontrada.')

cartao=input('O cartão informado é o Tabajara?(sim/não) ').lower().strip()

if cartao=='sim':
    desconto=kg*0.05
    kg-=desconto
    print('O total com desconto foi {:.2f} reais.'.format(kg))
else:
    print('O total foi {:.2f} reais.'.format(kg))
    