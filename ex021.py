nome = str(input('Digite o seu nome:\n')).strip()
print('Então seu nome em caps lock é',nome.upper())
print('Então seu nome em minusculo é...:',nome.lower())
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
nome2 = nome.split()
print('Seu primeiro nome é {}, e tem {} letras'.format(nome2[0],len(nome2[0])))

