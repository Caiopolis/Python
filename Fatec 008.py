### Lista 4 ###
##### Atividade 2 ######

print('Aqui vamos retornar o nome do Mês, com base no numero selecionado')
x = int(input('Digite um numero de sua preferencia (1 a 12)\n'))
while x > 12 or x == 0:
    print('Por favor, Digite os numeros entre os ()')
    x = int(input('Digite um numero de sua preferencia (1 a 12)\n'))

if x == 1:
    print(f'{x} se refere a Janeiro')
if x == 2:
    print(f'{x} se refere a Fevereiro')
if x == 3:
    print(f'{x} se refere a Março')
if x == 4:
    print(f'{x} se refere a Abril')
if x == 5:
    print(f'{x} se refere a Maio')
if x == 6:
    print(f'{x} se refere a Junho')
if x == 7:
    print(f'{x} se refere a Julho')
if x == 8:
    print(f'{x} se refere a Agosto')
if x == 9:
    print(f'{x} se refere a Setembro')
if x == 10:
    print(f'{x} se refere a Outubro')
if x == 11:
    print(f'{x} se refere a Novembro')
if x == 12:
    print(f'{x} se refere a dezembro')
per = str(input('deseja continuar?\n'))
while per != 'Não' and per != 'não':
    x = int(input('Digite um numero de sua preferencia (1 a 12)\n'))
    while x > 12 or x == 0:
        print('Por favor, Digite os numeros entre os ()')
        x = int(input('Digite um numero de sua preferencia (1 a 12)\n'))
    if x == 1:
        print(f'{x} se refere a Janeiro')
    if x == 2:
        print(f'{x} se refere a Fevereiro')
    if x == 3:
        print(f'{x} se refere a Março')
    if x == 4:
        print(f'{x} se refere a Abril')
    if x == 5:
        print(f'{x} se refere a Maio')
    if x == 6:
        print(f'{x} se refere a Junho')
    if x == 7:
        print(f'{x} se refere a Julho')
    if x == 8:
        print(f'{x} se refere a Agosto')
    if x == 9:
        print(f'{x} se refere a Setembro')
    if x == 10:
        print(f'{x} se refere a Outubro')
    if x == 11:
        print(f'{x} se refere a Novembro')
    if x == 12:
        print(f'{x} se refere a dezembro')
    per = str(input('deseja continuar?\n'))




