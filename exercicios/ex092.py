from datetime import  datetime
dados = dict()
dados['nome'] = str(input('Nome:  '))
nasc = int(input('Ano de nascimento:  '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (SE NAO TIVER DIGITE 0): '))
if dados['ctps'] != 0:
    dados['contratção'] = int(input('Ano  de Contratação: '))
    dados['salario'] = int(input('Salario: R$'))
    dados['aposentoria'] = dados ['idade'] + (dados['contratção'] + 35) - datetime.now().year
print('-=' * 30)
for k, v in dados.items():
    print(F' - {k} tem o valor {v}')
