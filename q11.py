#11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus 
#colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#    -salários até R$ 280,00 (incluindo) : aumento de 20%
#    -salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    -salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    -salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#    o salário antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo salário, após o aumento. 

#RECEBENDO O SALARIO ANTIGO
salarioAntigo=float(input('Informe o seu salário atual: '))

#CONSTANTES
aumento=0
porcentagem=0
salarioAtual=0
diferença=0
#salários até R$ 280,00 (incluindo) : aumento de 20%
if salarioAntigo<=280:
    aumento=salarioAntigo*0.2
    porcentagem=20
    salarioAtual=salarioAntigo+aumento
    print('\nO salário antes do reajuste {0} reais. '
    '\nO percentual de aumento aplicado {1} porcento. '
    '\nO valor do aumento foi de {2} reais. '
    '\nO novo salário, após o aumento ficou {3} reais'
    .format(salarioAntigo,porcentagem,aumento,salarioAtual))
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
elif salarioAntigo>280 and salarioAntigo<=700:
    aumento=salarioAntigo*0.15
    porcentagem=15
    salarioAtual=salarioAntigo+aumento
    print('\nO salário antes do reajuste {0} reais. '
    '\nO percentual de aumento aplicado {1} porcento. '
    '\nO valor do aumento foi de {2} reais. '
    '\nO novo salário, após o aumento ficou {3} reais'
    .format(salarioAntigo,porcentagem,aumento,salarioAtual))
#    -salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
elif salarioAntigo>=700 and salarioAntigo<=1500:
    aumento=salarioAntigo*0.1
    porcentagem=10
    salarioAtual=salarioAntigo+aumento
    print('\nO salário antes do reajuste {0} reais. '
    '\nO percentual de aumento aplicado {1} porcento. '
    '\nO valor do aumento foi de {2} reais. '
    '\nO novo salário, após o aumento ficou {3} reais'
    .format(salarioAntigo,porcentagem,aumento,salarioAtual))
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
elif salarioAntigo>=1500:
    aumento=salarioAntigo*0.05
    porcentagem=5
    salarioAtual=salarioAntigo+aumento
    print('\nO salário antes do reajuste {0} reais. '
    '\nO percentual de aumento aplicado {1} porcento. '
    '\nO valor do aumento foi de {2} reais. '
    '\nO novo salário, após o aumento ficou {3} reais'
    .format(salarioAntigo,porcentagem,aumento,salarioAtual))