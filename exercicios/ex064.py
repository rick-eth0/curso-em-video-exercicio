num = cont = soma =  0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
print('Vce digitou {} numeros e a sima entres els foi {}.'.format(cont, soma))


