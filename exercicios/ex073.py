times = ('corinthins', 'ṕalmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atletico', 'Botafgo', 'Atletico-PR', 'Bhaia',
         'Sao paulo', 'Fluminence', 'Sport Recife',
         'EC vitoria', 'Coritiba', 'Avai', 'Ponte preta',
         'Atletico-GO')
print('-=' * 15)
print(f'Lista de times do brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros sao {times[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimo sao {times[-4:]} ')
print('-=' * 15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense esta na {times.index("Chapecoense")+1}ª posição')

