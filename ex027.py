velocidade_carro = int(input('Qual a velocidade do carro?\n'))
if velocidade_carro > 80:
    print('Você estava acima da velocidade permitida\n'
          'a multa é de 7,00 reias por KM acima!')
    velocidade_carro2 = velocidade_carro - 80
    velocidade_carro2 = velocidade_carro2 * 7.00
    preco = velocidade_carro2
    print('o preço que vai pagar é de R${:.2f}'.format(preco))
else:
    print('Esta tudo certo! Boa viagem!')