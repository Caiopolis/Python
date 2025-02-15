import random
x = random.randint(0,5)
escolha = int(input('Digite o numero pensado pelo programa!!\n'
                    'ele vai de 0 a 5, Boa sorte!!\n'))
if escolha == x:
    print('Uau, Você acertou, PARABENS!!')
else:
    print('Que pena! Você errou ;-;')