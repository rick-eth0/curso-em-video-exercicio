casa = float(input('valor da casa: R$'))
salario = float(input('salario do comprsrdor: R$'))
anos = int(input('Quantos anos de financeiramente? '))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestaçao sera de R${:.2f}'.format(prestaçao))
if prestaçao <= minimo:
    print('Emprestimo pode ser \033[1;34mCONCEDIDO!\033[m')
else: print('Emprestimo NEGADO!')
