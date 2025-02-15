num = int(input('Digite um numero que vamos retornar se o mesmo é par ou impar:\n'))
impar_par = num % 2
if impar_par == 1:
    print('Este numero é impar')
else:
    print('Este numero é par')