 #total = 0
 #print('''Óla, aqui vamos calcular a média de 20 funcionarios, em relação com seu salario'
 #Vamos começar''')
 #for salario2 in range(1,20+1):
 #salario = float(input('Qual o seu salario?\n'))
 #total = salario + total
 #total2 = total/20

 #print('A média dos 20 funcionarios é R${:,.2f}'.format(total2))



print('Olá, aqui vamos reajustar o seu salario, com uma taxa de 8%')
nome = str(input('Qual o seu nome?\n')).strip().capitalize()
salario = float(input('Qual o seu salario atual?\n'))
total = salario * 0.08
print('{} Seu novo salario é R$ {:,.2f}'.format(nome,total + salario))
per = str(input('Deseja realizar novos reajustes?\n')).strip().lower()
while per == 'sim':
 print('Ok, vamos lá')
 nome = str(input('Qual o seu nome?\n')).strip().capitalize()
 salario = float(input('Qual o seu salario atual?\n'))
 total = salario * 0.08
 print('{} Seu novo salario é R$ {:,.2f}'.format(nome, total + salario))
 per = str(input('Deseja realizar novos reajustes?\n')).strip().lower()
else:
 print('Espero ter ajudado')



totalc = 0
totalv = 0
print('Vamos calcular o preço de venda e de compra!')
for x in range(1,10+1):
 compra = float(input('Qual o valor da compra?\n'))
 totalc = compra + totalc
 venda = float(input('Qual o valor da venda?\n'))
 totalv = venda + totalv
 lucro = venda - compra
 if lucro <= 0:
  print('Não houve lucro')
 else:
  print('Houve lucro')
  lucro2 = compra * 0.15
 if lucro2 <= lucro:
  print('Houve um lucro de 15% ou mais')
 else:
  print('Não houve lucro de 15%')
  print('O valor de compra dos 10 produtos é R${:,.2f}\n'.format(totalc))
  print('O valor de venda dos 10 produtos é R${:,.2f}'.format(totalv))


num = 98
print('Olá, Aqui vamos testar sua sorte, existe um numero secreto, entre 0 a 100, '
'tente acertar!')
num2 = int(input('Digite um numero de 0 a 100:\n'))
while num2 != num:
 print('Infelizmente não é este! tente novamente')
 num2 = int(input('Digite um numero de 0 a 100:\n'))
else:
 print('PARABÉNS V0CÊ ACERTOU')


peso = 0
capacidade = 0
print('''Olá, aqui vamos verificar a quantidade de caixas e o seu peso,
referente aos limites suportados pelos caminhões, vamos lá!''')

peso2 = float(input('Digite o numero de caixas, totais, que serão inseridas:\n'))
peso = peso2 + peso
capacidade2 = int(input('Digite a quantidade, em toneladas, de caixas:\n'))
capacidade = capacidade + capacidade2
media = capacidade/peso
per = str(input('Há mais alguma caixa?\n')).lower()
while per == 'sim':
 print('Ok, porem, se lembre do limite do caminhão!')
 peso2 = float(input('Digite o numero de caixas, totais, que serão inseridas:\n'))
 peso = peso2 + peso
 capacidade2 = int(input('Digite a quantidade, em toneladas, de caixas:\n'))
 capacidade = capacidade + capacidade2
 media = capacidade/peso
 per = str(input('Há mais alguma caixa?\n')).lower()
else:
 print('Certo, vamos conferir')
 if peso > 200 or capacidade > 10:
  print('Infelizmente, algum dos paramentros se execedeu, verifique {} ou {} estão passando do limite'.format(peso,capacidade))
 else:
  print('Otimo! os paramentros estão corretos o numero de caixas é {}\n'
  'O peso em toneladas é {}\n'
 'E a Média dos vulumes é {} toneladas por caixa'.format(peso,capacidade,media))



idBoiGordo = 0
pesoBoiGordo = 0
idBoiMagro = 0
pesoBoiMagro = float('inf')
print('Olá, aqui vamos ler o Id e o peso de 90 Bois, e no final retornar qual o boi mais gordo e o boi mais magro\n'
      'Junto com seu numero de identificação')

for x in range(1, 3):
    idBoi = int(input("Digite a identificação do boi {}: ".format(x)))
    pesoBoi = float(input("Digite o peso do boi {}: ".format(x)))
    if pesoBoi > pesoBoiGordo:
        idBoiGordo = idBoi
        pesoBoiGordo = pesoBoi
    if pesoBoi < pesoBoiMagro:
        idBoiMagro = idBoi
        pesoBoiMagro = pesoBoi
print()
print("Boi mais gordo:")
print("Identificação:", idBoiGordo)
print("Peso:", pesoBoiGordo)
print()

print("Boi mais magro:")
print("Identificação:", idBoiMagro)
print("Peso:", pesoBoiMagro)


from math import factorial
print('Olá, Aqui vamos apresentar varios numero e seu fatorial')
x = int(input('Digite um numero\n'))
f = factorial(x)
print('O fatorial de {} é {:,.2f}'.format(x, f))
while x > 1:
  x = int(input('Digite um numero\n'))
  f = factorial(x)
  print('O fatorial de {} é {:,.2f}'.format(x,f))
else:
    print('FIM DO PROGRAMA')


salariobota = 0
fluminense = 0
botafogo = 0
vasco = 0
flamengo = 0
outros = 0
rj = 0
niteroi = 0
outros2 = 0
rt = 0
nf = 0
per = 'sim'
while per == 'sim':
    print('Vamos realizar uma pesquisa de opinião')
    print('''Qual o seu time do Coração?'
          1 - Fluminense
          2 - Botafogo
          3 - Vasco 
          4 - Flamengo
          5 - Outros''')
    time = int(input('Digite o numero do seu time\n'))
    if time == 1:
        fluminense = fluminense + 1
        salario = float(input('E qual o seu Salario?\n'))

    if time == 2:
        botafogo = botafogo + 1
        salario = float(input('E qual o seu Salario?\n'))

        salariobota = (salario + salariobota) / botafogo
    if time == 3:
        vasco = vasco + 1
        salario = float(input('E qual o seu Salario?\n'))

    if time == 4:
        flamengo = flamengo + 1
        salario = float(input('E qual o seu Salario?\n'))

    if time == 5:
        outros = outros + 1
        salario = float(input('E qual o seu Salario?\n'))

    print('''Legal! Agora aonde você mora?
              1 - RJ
              2 - Niterói
              3 - Outros''')
    lugar = int(input('Digite o numero do seu local\n'))
    if lugar == 1:
        rj =rj + 1
    if lugar == 2:
        niteroi = niteroi + 1
    if lugar == 3:
        outros2 = outros2 + 1
    if time == 5 and lugar == 1:
        rt = rt + 1
    if time == 1 and lugar == 2:
        nf = nf + 1
    per = str(input('Deseja continuar?\n')).lower()



print('''Farei um resumo desta pesquisa:
    Torcedores do Fluminense: {}
    Torcedores do Botafogo: {}
    Torcedores do Vasco: {}
    Torcedores do Flamengo: {}
    Torcedores de outros: {}'''.format(fluminense, botafogo, vasco, flamengo, outros))
print('    O número de pessoas moradoras do Rio de Janeiro, torcedores de outros clubes é {}'.format(rt))
print('    O número de pessoas moradoras de Niterói, torcedores do fluminense é {}'.format(nf))
print('    O Salario médio dos torcedores do Botafogo é R${:,.2f}'.format(salariobota))