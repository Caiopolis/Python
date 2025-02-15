num = int(input('Digite um numero:\n'))

while num > 9999 :
    print('ERRO')
    num = int(input('Digite um numero:\n'))
    if num > 9999 :
     print('Deu ERRO rapaz, tenta um numero menor ai!!')
     num = int(input('Digite um numero:\n'))
     if num > 9999 :
         print('To avisando, se continuar...')
         num = int(input('Digite um numero:\n'))
         if num > 9999 :
            print('Você...está de brincadeira...')
            num = int(input('Digite um numero menor que 9999:\n'))
            if num > 9999 :
                print('Ultima tentativa...se não...')
                per = str(input('Vai continuar com essa brincadeira mesmo?\n')).lower()
                while per != 'não':
                 print('VOCÊ FOI AVISADOO')
                if per == 'não':
                  print('ok, vamos lá...novamente...')
                  num = int(input('Digite um numero:\n'))

else:
 n = str(num)
 print('{} unidades'.format(n[3]))
 print('{} dezenas'.format(n[2]))
 print('{} centena'.format(n[1]))
 print('{} milhar'.format(n[0]))