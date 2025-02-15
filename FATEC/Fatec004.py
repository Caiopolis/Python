###### Atividade 1: ######

#for x in range(100,200):
 #if(x%2 == 1):
  #print(x)

###### Atividade 2: ######

calculo = 0
for x in range (1,501,2):
   if x % 3 == 0:
     calculo = calculo + x
print(calculo)


###### Atividade3: ######

#altura_boa_mulheres = 0
#homens_altos = 0
#maior_altura = 0


#for i in range(15):
    #altura = float(input("Digite a altura da pessoa {}: ".format(i+1)))
   # sexo = input("Digite o sexo da pessoa (H/M): ").upper()
    #if altura > maior_altura:
       # maior_altura = altura
    #if sexo == 'M' and altura > 1.65:
       # altura_boa_mulheres = 1 + altura_boa_mulheres
    #if sexo == 'H' and altura > 1.85:
        #homens_altos = 1 + homens_altos
#print("Quantidade de mulheres mais altas que 1.65: {}".format(altura_boa_mulheres))
#print("Quantidade de homens mais altos que 1.85: {}".format(homens_altos))
#print("Maior altura lida entre todas as pessoas: {}".format(maior_altura))

##### Atividade 4: ######

import emoji
print('Olá, Aqui vamos fazer alguns calculos de temperatura. \nComo transformar elas em Celsius ou kelvin ou Fahrenheit')
per = str(input('Qual temperatura deseja transformar? '))
if per != 'Celsius' and per != 'Fahrenheit' and per != 'Kelvin':
    print('Não reconhecemos, por favor digite os termos: Celsius ou Fahrenheit ou Kelvin')
if per == 'Celsius':
    print('Certo!!')
    c = float(input('Quantos Graus Celsius deseja transformar? '))
    print('interessante...')
    cf = (c * 9 / 5) + 32
    ck = c + 273.15
    print('{}° Celsius em Fahrenheit é {}°F \nE em Kelvin são {:.2f}'.format(c, cf, ck))
if per == 'Fahrenheit':
    print('Certo!!')
    y = float(input('Quantos Graus Fahrenheit deseja transformar? '))
    print('interessante...')
    yc = (y - 32) * 5 / 9
    yk = (y - 32) * 5 / 9 + 273.15
    print('{}° Fahrenheit em Celsius é {:.2f}°C \nE em Kelvin são {:.2f}'.format(y, yc, yk))
if per == 'Kelvin':
    print('Certo!!')
    k = float(input('Quantos Kelvin deseja transformar? '))
    print('interessante...')
    kf = (k - 273.15) * 9 / 5 + 32
    kc = k - 273.15
    print('{} Kelvin em Celsius é {:.2f}°C \nE em Fahrenheit são {:.2f}°F'.format(k, kc, kf))
per2 = str(input('Deseja continuar? '))
while per2 != 'Não' and per2 != 'não':

    per = str(input('Qual temperatura deseja transformar? '))
    if per != 'Celsius' and per != 'Fahrenheit' and per != 'Kelvin':
        print('Não reconhecemos, por favor digite os termos: Celsius ou Fahrenheit ou Kelvin')
    if per == 'Celsius':
        print('Certo!!')
        c = float(input('Quantos Graus Celsius deseja transformar? '))
        print('interessante...')
        cf = (c * 9 / 5) + 32
        ck = c + 273.15
        print('{}° Celsius em Fahrenheit é {}°F \nE em Kelvin são {:.2f}'.format(c, cf, ck))
    if per == 'Fahrenheit':
        print('Certo!!')
        y = float(input('Quantos Graus Fahrenheit deseja transformar? '))
        print('interessante...')
        yc = (y - 32) * 5 / 9
        yk = (y - 32) * 5 / 9 + 273.15
        print('{}° Fahrenheit em Celsius é {:.2f}°C \nE em Kelvin são {:.2f}'.format(y, yc, yk))
    if per == 'Kelvin':
        print('Certo!!')
        k = float(input('Quantos Kelvin deseja transformar? '))
        print('interessante...')
        kf = (k - 273.15) * 9 / 5 + 32
        kc = k - 273.15
        print('{} Kelvin em Celsius é {:.2f}°C \nE em Fahrenheit são {:.2f}°F'.format(k, kc, kf))
    per2 = str(input('Deseja continuar? '))
print(emoji.emojize('Espero ter ajudado 😎🤓'))
