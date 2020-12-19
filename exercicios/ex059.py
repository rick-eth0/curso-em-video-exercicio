from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>>>>> Qual é a sua opcao? '))
    if opcao == 1: #somando
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2: #multiplicando
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3: #maior
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o Maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente.')
    print('=-=' * 10)
    sleep(1.75)
print('Fim do programa! Volte sempre! ')
