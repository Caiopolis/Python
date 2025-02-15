x1 = float(input('Aqui vamos calcular a área de um quarto retângular \nE verificar a quantidade de tinta necessaria '
                 '\nQual a altura? '))
x2 = float(input('Qual a largura? '))
x3 = x1*x2
print('A área do seu comodo é igual a {}m2'.format(x3))
print('OBS: A questão deu o dado... 1 litro pinta 2m^2')
print('Então irá precisar de {} litros'.format(x3/2))

