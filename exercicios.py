import os

print('Classificador:\n')
idade = int(input('Digite a sua idade: '))
if idade <= 12:
    os.system('cls')
    print('Você é uma criança\n')
elif idade >= 13 and idade <= 18:
    os.system('cls')
    print('Você é um adolescente\n')
else:
    os.system('cls')
    print('Você é um adulto\n')