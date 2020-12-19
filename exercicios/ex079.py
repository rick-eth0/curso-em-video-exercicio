'''numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso... ')
    else:
        print('Valor duplicado! nao vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')
print('-=' * 30)
'''

while True:
    respostap = str(input('   Deseja cadastrar outra pessoa? [S/N] ')).upper()
    if respostap != 'SsNn':
        break