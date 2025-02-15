km = int(input('Quantos KM dura sua viagem?\n'))
if km <= 200:
    km_pedagio = km * 0.50
    print('O preço total de sua viagem de {}KM, pelos pedagios é de R${}'.format(km,km_pedagio))
else:
    km_pedagio = km * 0.45
    print('O preço total de sua viagem de {}KM, pelos pedagios é de R${}'.format(km,km_pedagio))