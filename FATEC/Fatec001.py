# Geometria.
# Caio Henrique Arruda Moreira.
# Calculos Geométricos.

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
