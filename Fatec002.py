# Impar ou Par
# Caio Henrique Arruda Moreira
# Definir um termo como impar ou par.
# % = Mod.

print('Aqui iremos definir se o seu numero é impar ou par\n')
mod = int(input('Digite o numero que deseja analisar: '))
x = mod % 2

if x == 0:
    print('O resto da divisão do seu numero é {}, logo {} é par'.format(x, mod))
else:
    print('O resto da divisão do seu numero é {}, logo {} é impar'.format(x, mod))
