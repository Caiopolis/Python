print('Olá, este programa irá lhe ajudar a calcular o aumento do seu salário')
x = float(input('primeiramente, qual o seu salario, senhor(a)? '))
x2 = float(input('E quanto é a porcentagem de aumento? (Obs:Somente o numero,sem o simbolo da porcentagem) '))
print('Seu salário antigo era {}, com o aumento de {}%, seu novo salário é {}'.format(x,x2,x+x*(x2/100)))