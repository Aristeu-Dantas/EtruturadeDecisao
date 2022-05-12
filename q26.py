# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#     Álcool:
#     até 20 litros, desconto de 3% por litro
#     acima de 20 litros, desconto de 5% por litro
#     Gasolina:
#     até 20 litros, desconto de 4% por litro
#     acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina 
# é R$ 2,50 o preço do litro do álcool é R$ 1,90. 

#RECEBENDO DADOS
comb = input('Qual o tipo de combustivel?').upper()
l = float(input('Quantos litros foi colocado?'))

#CALCULANDO
if comb == 'A':
    p=float((l*1.90))
    if p <= 20:
        p=p-(3/100*p)
    else:
        p=p-(4/100*p)
    print(p)

if comb == 'G':
    p=float((l*2.50))
    if p <= 20:
        p=p-(4/100*p)
    else:
        p=p-(6/100*p)
    print(p)





