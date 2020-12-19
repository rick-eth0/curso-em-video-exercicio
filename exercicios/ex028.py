from random import randint
from time import sleep
perg = 0
computador = randint(0, 5) #Faz o computador "pensar"
print('\033[1;35m-=-\033[m' * 20)
print('Vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('\033[1;35m-=-\033[m' * 20)
jogador = int(input('Em que numero eu pensei? ')) # jogador tenta adivinhar
print('\033[1;30mPROCESSANDO...\033[m')
sleep(1.5)
while jogador == computador:
    print('\033[1;36mPARABENS!\033[m Voce conseguiu venser! ')

     print('\033[1;31mVOCE PERDEU!\033[m Eu pensei no numero {} e nao no {}'.format(computador, jogador ))
