#04 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

#Recebendo o caractere
char=str(input('Informe um caractere: ').lower())

if char.isalpha():
    if char == 'a':
        print('O caractere é uma vogal.')
    elif char == 'e':
        print('O caractere é uma vogal.')
    elif char == 'i':
        print('O caractere é uma vogal.')
    elif char == 'o':
        print('O caractere é uma vogal.')
    elif char == 'u':
        print('O caractere é uma vogal.')
    else:
        print('Caractere encontrado é uma consoantea.')
else:
    print('O carctere informado é um numero')