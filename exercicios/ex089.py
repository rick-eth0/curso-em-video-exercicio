from time import sleep
ficha = list()
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota: '))
    nota2 = float(input('nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar?  [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 35)
    opc = int(input('Mostre notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        sleep(1.5)
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

























