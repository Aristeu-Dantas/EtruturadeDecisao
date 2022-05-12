# 25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#    a-"Telefonou para a vítima?"
#    b-"Esteve no local do crime?"
#    c-"Mora perto da vítima?"
#    d-"Devia para a vítima?"
#    e-"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
# participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário,
# ele será classificado como "Inocente".

# FAZENDO AS PERGUNTAS
from itertools import count


p1 = str(input('Telefonou para a vítima? ')).lower().strip()
p2 = str(input('Esteve no local do crime? ')).lower().strip()
p3 = str(input('Mora perto da vítima? ')).lower().strip()
p4 = str(input('Devia para a vítima? ')).lower().strip()
p5 = str(input('Já trabalhou com a vítima? ')).lower().strip()

# LÓGICA
resposta = []
if p1 == 'sim':
    resposta.append(1)
else:
    resposta.append(0)

if p2 == 'sim':
    resposta.append(1)
else:
    resposta.append(0)

if p3 == 'sim':
    resposta.append(1)
else:
    resposta.append(0)

if p4 == 'sim':
    resposta.append(1)
else:
    resposta.append(0)

if p5 == 'sim':
    resposta.append(1)
else:
    resposta.append(0)


print(resposta.count(1))


##print('Na frase a palavra "sim" {0} vezes.'.format(construtor.count('sim')))

if resposta.count(1)==2:
    print('Pessoa é suspeita.')
elif resposta.count(1)==3 or resposta.count(1)==4:
   print('Pessoa é cúmplice')
elif resposta.count(1)==5:
    print('Pessoa é culpada.')
elif resposta.count(1)==1 or resposta.count(1)==0:
    print('Pessoa é inocente.')
