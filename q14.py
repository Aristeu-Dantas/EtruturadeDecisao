#14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa 
# disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:

#      Média de Aproveitamento  Conceito
#      Entre 9.0 e 10.0        A
#      Entre 7.5 e 9.0         B
#      Entre 6.0 e 7.5         C
#      Entre 4.0 e 6.0         D
#      Entre 4.0 e zero        E

#O algoritmo deve mostrar na tela as notas, a média,
#o conceito correspondente e a mensagem “APROVADO” se o conceito for A,
#B ou C ou “REPROVADO” se o conceito for D ou E.

#RECEBENDO NOTAS
nota1=float(input('Informa a sua primeira nota: '))
nota2=float(input('Informa a sua segunda nota: '))

media=(nota1+nota2)/2

print('Média de Aproveitamento  Conceito')
#CALCULANDO
if media>=9 or media<=10:
    print('Média {0}  A'
    '\nAPROVADO! '.format(media))  
elif media>=7.5 or media<=8.9:
    print('Média {0}  B'
    '\nAPROVADO! '.format(media))
elif media>=6 or media<=7.4:
    print('Média {0}  C'
    '\nAPROVADO! '.format(media))
elif media>=4 or media<=5.9:
    print('Média {0}  D'
    '\nREPROVADO! '.format(media))
elif media>=0 or media<=3.9:
    print('Média {0}  E'
    '\nREPROVADO! '.format(media))