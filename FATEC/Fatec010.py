# print('Minha primeira aplicação em Python')


# print(2*23454)
# print(10000+23432)
# print(1897/2)
# print(18900 - 1200)
# print(123-564+(290*3)/4)
# print(22 % 2)
# print(234 // 3)
# print(2**9)


# print(''' Opções:
# -h    -oi   -ola
# -Python -Java''')


# print((10 * 'Py') + (10 * 'thon'))


# frase = str(input('Digite seu nome:\n')).split()
# print('Seu primeiro nome é {} '.format(frase[0]))
# print('Seu segundo nome é {} '.format(frase[1]))
# print('A primeira letra do seu nome é {} '.format(' '.join(frase)[0]))
# print('Seu nome fica assim, indo de 2 em 2: {}'.format(' '.join(frase)[::2]))
# print('Seu nome tem no total {} letras (contando o spaço)'.format((len(' '.join(frase)))))


# lista = [1,2,3,4,5,6,7,8,9]
# print(lista[:2])
# print(lista[::2])
# print(lista)
# lista.append(10)
# print(lista)
# print(len(lista))


# nome = str(input('Digite o seu nome (Não digite Caio...Cuidado)\n')).lower()
# while nome == 'caio':
# print('NÃOOOOO, ESSE NOME NÃO')
# else:
# print('Que nome bonito!!')


print('Aqui vamos definir quem recebe, ou não, uma cesta, dependendo da idade, e da cidade')
idade = int(input('Qual sua idade?\n'))
cidade = str(input('Qual sua cidade?\n')).lower()
cestas = 0
if idade >= 60 and cidade == 'caxingui':
    print('Otimo, voce ira receber')
    cestas = cestas + 1
    per = str(input('Quer insirir mais outra peessoa?\n')).lower()
    while per == 'sim' and idade >= 60 and cidade == 'caxingui':
        print('Ok, vamos novamente:')
        idade = int(input('Qual sua idade?\n'))
        cidade = str(input('Qual sua cidade?\n')).lower()
        if idade >= 60 and cidade == 'caxingui':
            print('Otimo, voce ira receber')
            cestas = cestas + 1
            per = str(input('Quer insirir mais outra peessoa?\n')).lower()
        else:
            print('Ok, foram entregues {} cestas'.format(cestas))
    else:
        print('Ok, foram entregues {} cestas'.format(cestas))
else:
    print('Ok, foram entregues {} cestas'.format(cestas))

# num = int(input('Digite um numero:\n'))
# for num2 in range(num,50+1):
# print(num2)


# num = int(input('Digite um numero: '))
# while num > 100:
#   print('Erro')
#    num = int(input('Digite um numero menor que 100: '))
# else:
#  for num2 in range(num,100,3):
#     print(num2)
#  per = str(input('Deseja começar com um numero diferente?(sim ou não)\n')).lower()
#  while per == 'sim':
#     num = int(input('Digite um numero: '))
#     while num > 100:
#      print('Erro')
#      num = int(input('Digite um numero menor que 100: '))
#     else:
#      for num2 in range(num,100,3):
#       print(num2)
#      per = str(input('Deseja começar com um numero diferente?(sim ou não)\n'))
#  else:
#    print('Obrigado, espero ter ajudado')
