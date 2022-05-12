#12 - Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) 
# e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#    Desconto do IR:
#    Salário Bruto até 900 (inclusive) - isento
#    Salário Bruto até 1500 (inclusive) - desconto de 5%
#    Salário Bruto até 2500 (inclusive) - desconto de 10%
#    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
#  dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220. 

# Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

#RECEBENDO AS INFORMAÇÕES
valor=float(input('Quanto você ganha por hora? '))
horas=int(input('Quantas horas você trabalha por semana?'))*4

#CONSTANTES
IR=0
INSS=0
FGTS=0
saldoB= valor*horas
#CALCULANDO
#    Salário Bruto até 900 (inclusive) - isento
if saldoB<=900:
    IR=0
    INSS=saldoB*0.1
    FGTS=saldoB*0.11
    totalD=IR+INSS
    saldoL=saldoB-(IR+INSS)
    print('\nSalário Bruto:                 : R$  {0},00'
         '\n(-) IR (0%)                     : R$  {1},00'
         '\n(-) INSS ( 10%)                 : R$  {2},00'
         '\nFGTS (11%)                      : R$  {3},00'
         '\nTotal de descontos              : R$  {4},00'
         '\nSalário Liquido                 : R$  {5},00'
         .format(saldoB,IR,INSS,FGTS,totalD,saldoL))
#Salário Bruto até 1500 (inclusive) - desconto de 5%
elif saldoB>900 and saldoB<=1500:
    IR=saldoB*0.05
    INSS=saldoB*0.1
    FGTS=saldoB*0.11
    totalD=IR+INSS
    saldoL=saldoB-(IR+INSS)
    print('\nSalário Bruto:                 : R$  {0},00'
         '\n(-) IR (5%)                     : R$  {1},00'
         '\n(-) INSS ( 10%)                 : R$  {2},00'
         '\nFGTS (11%)                      : R$  {3},00'
         '\nTotal de descontos              : R$  {4},00'
         '\nSalário Liquido                 : R$  {5},00'
         .format(saldoB,IR,INSS,FGTS,totalD,saldoL))
#Salário Bruto até 2500 (inclusive) - desconto de 10%
elif saldoB>1500 and saldoB<=2500:
    IR=saldoB*0.1
    INSS=saldoB*0.1
    FGTS=saldoB*0.11
    totalD=IR+INSS
    saldoL=saldoB-(IR+INSS)
    print('\nSalário Bruto:                 : R$  {0},00'
         '\n(-) IR (10%)                    : R$  {1},00'
         '\n(-) INSS ( 10%)                 : R$  {2},00'
         '\nFGTS (11%)                      : R$  {3},00'
         '\nTotal de descontos              : R$  {4},00'
         '\nSalário Liquido                 : R$  {5},00'
         .format(saldoB,IR,INSS,FGTS,totalD,saldoL))
# Salário Bruto acima de 2500 - desconto de 20%
elif saldoB>2500:
    IR=saldoB*0.2
    INSS=saldoB*0.1
    FGTS=saldoB*0.11
    totalD=IR+INSS
    saldoL=saldoB-(IR+INSS)
    print('\nSalário Bruto:                 : R$  {0},00'
         '\n(-) IR (20%)                    : R$  {1},00'
         '\n(-) INSS ( 10%)                 : R$  {2},00'
         '\nFGTS (11%)                      : R$  {3},00'
         '\nTotal de descontos              : R$  {4},00'
         '\nSalário Liquido                 : R$  {5},00'
         .format(saldoB,IR,INSS,FGTS,totalD,saldoL))