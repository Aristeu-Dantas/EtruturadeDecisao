#03 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
#  F - Feminino, M - Masculino, Sexo Inválido. 

#Recebendo o genero
genero=str(input('Informe o seu genero convêncional com M ou F: ').upper())

#processando
if genero=='H':
    print('O seu genero é masculino.')
elif genero=='M':
    print('O seu genero é feminino.')
else:
    print('Genero não encontrado.')