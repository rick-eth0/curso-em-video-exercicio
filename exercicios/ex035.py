print('-='*20)
print('Analisador de triangulos ')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento acima PODEM FORMAR triangulo!')
else:
    print('Os segmento acima NAO PODEM FORMAR triangulo')
