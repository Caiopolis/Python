print('Olá, aqui vamos verificar se vc esta apto a reivindicar um empréstimo, para a compra de uma casa')
val_casa = int(input('Qual o valor da Casa?\n'))
sal_comprador = float(input('Qual o seu salario?\n'))
anos_pagar = int(input('Quantos anos vc pretende quitar a casa?\n'))
print('Obrigado pelas informações')
pagamento = val_casa/(anos_pagar*12)
if sal_comprador*30/100 < pagamento:
    print('Negado')
else:
    print('permitido')

