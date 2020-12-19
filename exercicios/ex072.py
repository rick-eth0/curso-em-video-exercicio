cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinci', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'desseseis', 'dessesete', 'dezoito',
        'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Tente novamnete. ', end='')
    while num not in 'SN':
        numm = str(input('deseja continuar? ')).strip().upper()[0]
        if num == 'N':
            break
            print('{:=^30}'.format('PROGRAMA FINALIZADO'))





















