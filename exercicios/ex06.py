from time import sleep
n = int(input('digite  um numero:'))
sleep(0.5)
print('o dobro de {} vale {}.'.format(n, (n*2)))
print('o triplo de {} vale {}. \na raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))
