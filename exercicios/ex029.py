velocidade = float(input('Qual é a velocidade atual do carro ?'))
if velocidade > 80:
    print('\033[1;31mMULTADO!\033[m voce excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar \033[4;30muma multa de R${:.2f}\033[m'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
