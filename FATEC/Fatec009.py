# Lista 4
# Atividade 3
import emoji

print('Olá, aqui teremos um pequeno programa, com varias opções')
escolha = 0
while escolha != 9:
    print(
        '[1] Tabuada\n [2] Calculos de geometria\n [3] soma com valor descrecente\n [4] conversão de temperatura\n ['
        '9] Fim do programa')
    escolha = int(input('Qual sua opção?\n'))
    if escolha == 1:
        print("Olá, aqui iremos lhe mostrar a tabúada do numero que desejar!")
        tabuada = int(input("Ok, digite o numerador que deseja averiguar a tabuada: "))
        print('| ' * 7)
        print('{} x {:2} = {}'.format(tabuada, 1, tabuada * 1))
        print('{} x {:2} = {}'.format(tabuada, 2, tabuada * 2))
        print('{} x {:2} = {}'.format(tabuada, 3, tabuada * 3))
        print('{} x {:2} = {}'.format(tabuada, 4, tabuada * 4))
        print('{} x {:2} = {}'.format(tabuada, 5, tabuada * 5))
        print('{} x {:2} = {}'.format(tabuada, 6, tabuada * 6))
        print('{} x {:2} = {}'.format(tabuada, 7, tabuada * 7))
        print('{} x {:2} = {}'.format(tabuada, 8, tabuada * 8))
        print('{} x {:2} = {}'.format(tabuada, 9, tabuada * 9))
        print('{} x {:2} = {}'.format(tabuada, 10, tabuada * 10))
        print('| ' * 7)
    if escolha == 2:
        print('olá, aqui vamos calcular formas geométricas')

        print('primeiramente vamos calcular a área de um retângulo\n')

        x = float(input('Digite a altura do retângulo: '))
        y = float(input('Digite a base do mesmo: '))
        s = x * y

        print('A área do retângulo é {}\n'.format(s))

        pergunta = str(input('Deseja continuar e realizar a área de um circulo? (sim ou não) digite: '))
        if pergunta == 'sim' or pergunta == 'Sim':
            print('Ótimo, Vamos lá\n')
            raio = float(input('Digite o raio da circunferência: '))
            z = 3.1416 * raio ** 2
            print('a área do circulo é {}\n'.format(z))
        pergunta2 = str(input('Deseja continuar e realizar o perimêtro de um quadrado? (Sim ou Não) digite: '))
        if pergunta2 == 'sim' or pergunta == 'Sim':
            print('Legal!')
            p1 = float(input('Digite o perimetro esquerdo do quadrado: '))
            p2 = float(input('Digite o perimetro direito do quadrado: '))
            p3 = float(input('Digite o perimetro de cima do quadrado: '))
            p4 = float(input('Digite o perimetro de baixo do quadrado: '))
            qua = p1 + p2 + p3 + p4
            print('o perimetro do quadrado é: {}\n'.format(qua))
        print('Obrigado, espero ter ajudado')
    if escolha == 3:
        lista = []
        x1 = int(input('Digite um valor '))
        x2 = int(input('Digite um valor para somar '))
        x3 = x1 + x2
        for x in range(1, x3 + 1):
            lista.append(x)
        lista.sort(reverse=True)

        print('A sequência decrescente é {}'.format(lista))
    if escolha == 4:
        import emoji

        print(
            'Olá, Aqui vamos fazer alguns calculos de temperatura. \nComo transformar elas em Celsius ou kelvin ou '
            'Fahrenheit')
        per = str(input('Qual temperatura deseja transformar? (C,F,K) '))
        if per != 'C' and per != 'F' and per != 'K':
            print('Não reconhecemos, por favor digite os termos: Celsius ou Fahrenheit ou Kelvin')
        if per == 'C':
            print('Certo!!')
            c = float(input('Quantos Graus Celsius deseja transformar? '))
            print('interessante...')
            cf = (c * 9 / 5) + 32
            ck = c + 273.15
            print('{}° Celsius em Fahrenheit é {}°F \nE em Kelvin são {:.2f}'.format(c, cf, ck))
        if per == 'F':
            print('Certo!!')
            y = float(input('Quantos Graus Fahrenheit deseja transformar? '))
            print('interessante...')
            yc = (y - 32) * 5 / 9
            yk = (y - 32) * 5 / 9 + 273.15
            print('{}° Fahrenheit em Celsius é {:.2f}°C \nE em Kelvin são {:.2f}'.format(y, yc, yk))
        if per == 'K':
            print('Certo!!')
            k = float(input('Quantos Kelvin deseja transformar? '))
            print('interessante...')
            kf = (k - 273.15) * 9 / 5 + 32
            kc = k - 273.15
            print('{} Kelvin em Celsius é {:.2f}°C \nE em Fahrenheit são {:.2f}°F'.format(k, kc, kf))
        per2 = str(input('Deseja continuar? '))
        while per2 != 'Não' and per2 != 'não':

            per = str(input('Qual temperatura deseja transformar? (C,F,K) '))
            if per != 'C' and per != 'F' and per != 'K':
                print('Não reconhecemos, por favor digite os termos: Celsius ou Fahrenheit ou Kelvin')
            if per == 'C':
                print('Certo!!')
                c = float(input('Quantos Graus Celsius deseja transformar? '))
                print('interessante...')
                cf = (c * 9 / 5) + 32
                ck = c + 273.15
                print('{}° Celsius em Fahrenheit é {}°F \nE em Kelvin são {:.2f}'.format(c, cf, ck))
            if per == 'F':
                print('Certo!!')
                y = float(input('Quantos Graus Fahrenheit deseja transformar? '))
                print('interessante...')
                yc = (y - 32) * 5 / 9
                yk = (y - 32) * 5 / 9 + 273.15
                print('{}° Fahrenheit em Celsius é {:.2f}°C \nE em Kelvin são {:.2f}'.format(y, yc, yk))
            if per == 'K':
                print('Certo!!')
                k = float(input('Quantos Kelvin deseja transformar? '))
                print('interessante...')
                kf = (k - 273.15) * 9 / 5 + 32
                kc = k - 273.15
                print('{} Kelvin em Celsius é {:.2f}°C \nE em Fahrenheit são {:.2f}°F'.format(k, kc, kf))
            per2 = str(input('Deseja continuar? '))
        print(emoji.emojize('Espero ter ajudado 😎🤓'))

print(emoji.emojize('Fim do programa, espero ter ajudado 😎🤓'))
