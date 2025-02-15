city = str(input('Qual a sua cidade?\n')).strip().capitalize()
city2 = city.split()
santo = 'Santo' in city2[0]
print(santo)