#05 - Faça um programa para a leitura de duas notas parciais de um aluno. 
#O programa deve calcular a média alcançada por aluno e apresentar:

#    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#    A mensagem "Reprovado", se a média for menor do que sete;
#    A mensagem "Aprovado com Distinção", se a média for igual a dez. 

#RECEBENDO AS NOTAS
nota1=float(input('Informe a sua primeira nota: '))
nota2=float(input('Informe a sua segunda nota: '))

#CALCULANDO A MÉDIA
media=(nota1+nota2)/2

#MENSAGEM
if media>=7:
    print('Aprovado')
elif media<7:
    print('Reprovado')
elif media==10:
    print('Aprovado com Distinção')
    