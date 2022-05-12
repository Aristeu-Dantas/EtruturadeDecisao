#Faça um Programa que peça os 3 lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#
#    Dicas:
#    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#    Triângulo Equilátero: três lados iguais;
#    Triângulo Isósceles: quaisquer dois lados iguais;
#    Triângulo Escaleno: três lados diferentes;

#RECEBENDO OS LADOS DO TRIANGULO
lado1=float(input('Informe o primeiro lado do triangulo: '))
lado2=float(input('Informe o segundo lado do triangulo: '))
lado3=float(input('Informe o terceiro lado do triangulo: '))

#VERIFICANDO SE OS LADOS INFORMADOS SÃO DE UM TRAINGULO
if lado1+lado2>lado3 or lado1+lado3>lado2 or lado2+lado3>lado1:
    print('As medidas informadas são de um triângulo.')
else:
    print('As medidas informadas não são de um triângulo.')

#VERIFICANDO O TIPO DE TRIANGULO
if lado1==lado2==lado3:
    print('O triângulo é equilátero.')
elif lado1==lado2!=lado3 or lado1==lado3!=lado2 or lado3==lado2!=lado1:
    print('O triângulo informado é isósceles.')
elif lado1!=lado2!=lado3:
    print('O triângulo é isósceles.')