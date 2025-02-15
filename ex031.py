print('Vamos reajustaro seu salario!')
salario = float(input('Qual o seu salario atual?\n'))
if salario > 1250:
    print('Ok, ira receber um aumento de 10%')
    salario_10 = salario * 0.1
    salario_atual = salario + salario_10
    print('Seu novo salario é de R${}'.format(salario_atual))
else:
    print('Ok,ira receber um aumento de 15%')
    salario_15 = salario * 0.15
    salario_atual = salario + salario_15
    print('Seu novo salario é de R${}'.format(salario_atual))