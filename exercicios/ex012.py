preço = float(input('Qual é o preço do produto?'))
novo = preço - ( preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% va custar R${:.2f}'.format(preço, novo))
