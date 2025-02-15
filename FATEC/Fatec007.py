### Lista 4 ###
##### Atividade 1 ######

print('Aqui vamos retornar o dia da semana, com base no numeo selecionado')
x = int(input('Digite um numero de sua preferencia (1 a 7)\n'))
while x > 7 or x == 0:
    print('Por favor, Digite os numeros entre os ()')
    x = int(input('Digite um numero de sua preferencia (1 a 7)\n'))

if x == 1:
    print(f'{x} se refere a domingo')
if x == 2:
    print(f'{x} se refere a segunda')
if x == 3:
    print(f'{x} se refere a terça')
if x == 4:
    print(f'{x} se refere a quarta')
if x == 5:
    print(f'{x} se refere a quinta')
if x == 6:
    print(f'{x} se refere a sexta')
if x == 7:
    print(f'{x} se refere a sábado')
per = str(input('deseja continuar?\n'))
while per != 'Não':
    x = int(input('Digite um numero de sua preferencia (1 a 7)\n'))
    while x > 7 or x == 0:
        print('Por favor, Digite os numeros entre os ()')
        x = int(input('Digite um numero de sua preferencia (1 a 7)\n'))
    if x == 1:
        print(f'{x} se refere a domingo')
    if x == 2:
        print(f'{x} se refere a segunda')
    if x == 3:
        print(f'{x} se refere a terça')
    if x == 4:
        print(f'{x} se refere a quarta')
    if x == 5:
        print(f'{x} se refere a quinta')
    if x == 6:
        print(f'{x} se refere a sexta')
    if x == 7:
        print(f'{x} se refere a sábado')
    per = str(input('deseja continuar?\n'))

