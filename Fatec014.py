numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
pares = list(filter(lambda x: x % 2 == 0, numeros))

impares = list(filter(lambda x: x % 2 != 0, numeros))
print("Números pares:")
for numero in pares:
    print(numero)
print("\nNúmeros ímpares:")
for numero in impares:
    print(numero)