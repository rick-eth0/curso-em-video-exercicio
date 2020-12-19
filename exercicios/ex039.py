from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar \033[1;31mIMEDIATAMENTE!\033[m ')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para ser feito o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deviria ter se alistado ha {} anos.'.format(saldo))
    ano = atual - saldo
    print(' Seu alistamento foi em {}'.format(ano))
