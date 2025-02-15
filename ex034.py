ano_nascimento = int(input('Em qual ano vc nasceu?\n'))
idade = 2024 - ano_nascimento
if idade == 18:
    print('Esta no momento de se alistar!')
elif idade < 18:
    print('Você não precisa se alistar no momento')
else:
    print('Já passou do tempo de se alistar, por favor, se aliste')