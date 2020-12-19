from time import sleep
def volto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos : NAO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f' com {idade} anos: VOLTO OPCIONAL! '
    else:
        return f' com {idade} anos: VOLTO OBRIGATORIO!'


# programa principal
nasc = int(input('Em qual ano voce nasceu?'))
print('Carregando...')
sleep(1.75)
print(volto(nasc))

