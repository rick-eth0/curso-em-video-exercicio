from random import randint
from time import sleep
import emoji
itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)
print(f'{itens[computador]}')
print('''Suas opçỗes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print(emoji.emojize('Computador jogando...:game_die:',use_aliases=True))
sleep(0.6)
print('JO')
sleep(0.75)
print('KEM')
sleep(0.75)
print('PO!!!')
sleep(0.75)
print('\033[1;32m-=\033[m' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('\033[1;32m-=\033[m' * 11)
if computador == 0: #computador jogou  PEDRA
    if jogador == 0:
        print('\033[1;31mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;34mJOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('\033[1;31mJOGADA INVALIDA!\033[m')
elif computador == 1:  #computador jogou  PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('\033[1;31mEMPATE\033[m')
    elif jogador == 2:
        print('\033[1;34mJOGADOR VENCEU\033[m')
    else:
        print(' \033[1;31mJOGADA INVALIDA!\033[m')
elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('\033[1;34mJOGADOR VENCEU\033[m')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('\033[1;31mEMPATE\033[m')
    else:
        print(' \033[1;31JOGADA INVALIDA\033[m')

