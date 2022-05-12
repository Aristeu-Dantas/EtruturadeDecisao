#19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
#  dezenas e unidades do mesmo.
#
#    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#    326 = 3 centenas, 2 dezenas e 6 unidades
#    12 = 1 dezena e 2 unidades Testar com: 
# 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

#RECEBENDO
numero=int(input('Informe um numero inteiro de 0 a 1000: '))

#DEFININDO CONSTANTES
unidade=numero%10
dezena=numero // 10%10
centena=numero // 100%10

#CALCULANDO
if numero<1000 or numero<0:
    print('O número inteiro informado tem {0} centenas, {1} dezenas e {2} unidades.'
    .format(centena,dezena,unidade))
else:
    print('ERRO!!')