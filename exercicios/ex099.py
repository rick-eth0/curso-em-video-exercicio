from time import sleep
def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analizando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    print(f'foam imformados {cont} valores ao todo.')
    print(f'O maior valor imformado foi {maior}.')


#programa principal
maior(2, 4, 7, 3, 9, 10)
maior(3, 28, 7)
maior(1, 5)
maior(0)

