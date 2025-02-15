print('Caio Henrique Arruda Moreira')
print('Fatec Zona Sul - Dom Paulo Evaristo Arns')



print('''|---------|
|         |
|   Caio  |
|         |
|---------|''')



x = 45 + 37 * 78 + 4 / 24
print('O resultada da operação é {:,.2f}'.format(x))



nome = str(input('Qual seu nome?\n'))
idade = int(input('Qual sua idade?\n'))
x = idade * 12 + 10
print('O resultado da Multiplicação da idade por 12 e adicionado 10 é igual a: {}'.format(x))




x = int(input('Qual o numro que deseja verificar?, se pe primo ou não:\n'))
primo = x % 2
if primo == 1:
    print('É um numero primo')
else:
    print('Não é um numero primo')
print('Vamos checar se você é de maior')
idade = int(input('Qual sua idade?\n'))
if idade >= 18:
    print('True')
else:
    print('False')

per = str(input('Quer refazer?\n')).lower()
while per == 'sim':
    print('Vamos lá')
    x = int(input('Qual o numro que deseja verificar?, se pe primo ou não:\n'))
    primo = x % 2
    if primo == 1:
        print('É um numero primo')
    else:
        print('Não é um numero primo')
    print('Vamos checar se você é de maior')
    idade = int(input('Qual sua idade?\n'))
    if idade >= 18:
        print('True')
    else:
        print('False')
    per = str(input('Quer refazer?\n')).lower()
else:
    print('Espero ter ajudado')