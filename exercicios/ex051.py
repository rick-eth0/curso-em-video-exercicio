primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão:  '))
decima = primeiro + (10 - 1) * razão
for c in range(primeiro, decima + razão, razão):
    print('{} '.format(c), end=' -> ')
print('ACABOU')
