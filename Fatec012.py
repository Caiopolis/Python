
mes = 0
nascimento = str(input('Digite o dia/mês/ano do seu nascimento (Coloque o //, exemplo dd/mm/aaaa):\n'))
dia = int(nascimento[0:2])
mes2 = int(nascimento[3:5])
if mes2 == 1:
    mes = "janeiro"
elif mes2 == 2:
    mes = "fevereiro"
elif mes2 == 3:
    mes = "março"
elif mes2 == 4:
    mes = "abril"
elif mes2 == 5:
    mes = "maio"
elif mes2 == 6:
    mes = "junho"
elif mes2 == 7:
    mes2 = "julho"
elif mes2 == 8:
    mes = "agosto"
elif mes2 == 9:
    mes = "setembro"
elif mes2 == 10:
    mes = "outubro"
elif mes2 == 11:
    mes = "novembro"
elif mes2 == 12:
    mes = "dezembro"

print('Data de nascimento: {} de {} de {}'.format(nascimento[0:2], mes, nascimento[6:10]))




def ler_string(numero):
    string = input(f"Digite a {numero}ª string: ")
    return string, len(string)


def comparar_strings(string1, string2):
    if string1 == string2:
        return "iguais"
    else:
        return "diferentes"


string1, comprimento1 = ler_string(1)
string2, comprimento2 = ler_string(2)


print(f"Conteúdo da primeira string: {string1}, Comprimento: {comprimento1}")
print(f"Conteúdo da segunda string: {string2}, Comprimento: {comprimento2}")


if comprimento1 == comprimento2:
    print("As duas strings possuem o mesmo comprimento.")
else:
    print("As duas strings possuem comprimentos diferentes.")


resultado_comparacao = comparar_strings(string1, string2)
print(f"As duas strings são {resultado_comparacao}.")


frase = str(input('Digite qualquer frase que quiser:\n')).strip().lower()
print('O numero de spaços que esta frase tem é igual a {}'.format(frase.count(' ')))
total_vogal = frase.count('a') + frase.count('e') + frase.count('i') + frase.count('o') + frase.count('u')
print('O numero de vogais que aparece é {}'.format(total_vogal))


count = 0
saldo = 0
media = 0



per = str(input('Vamos lá?(sim ou não)\n')).lower()
while per == 'sim':
    valor = float(input('digite um valor:\n'))
    count = count + 1
    saldo = saldo + valor
    per = str(input('Vamos lá?\n')).lower()
media = saldo / count
print('Foram digitados um total de {} valores'.format(count))
print('O saldo destes valores são {:,.2f}'.format(saldo))
print('A média destes numero é {:,.2f}'.format(media))

print('Calcular taxa/multa')

valor_prestacao = float(input('Qual o valor da prestação?\n'))
dias_atraso = int(input('Quantos dias de atraso?\n'))
multa = valor_prestacao * 0.02
juros = 0.0003333 * dias_atraso * valor_prestacao
total_pagar = multa + juros + valor_prestacao
print('Certo, aqui esta o resumo da sua taxa/multa')
print('O valor da sua prestação é {}\n'
      'Os dias de atraso foram de {}\n'
      'A multa a pagar pelo atraso é {}\n'
      'O juros pela demora do pagameto é {}\n'
      'O total a pagar ficou igual á {:,.0f}'.format(valor_prestacao,dias_atraso,multa,juros,total_pagar))

def calcular_imposto(rendimento):
    if rendimento <= 85528:
        imposto = rendimento * 0.18 - 556.02
    else:
        imposto = 14839.02 + (rendimento - 85528) * 0.32
    imposto_arredondado = round(imposto)
    if imposto_arredondado < 0:
        imposto_arredondado = 0
    return imposto_arredondado


rendimento = float(input("Digite o rendimento: "))
imposto_calculado = calcular_imposto(rendimento)
print("Imposto calculado:", imposto_calculado, "thalers")
