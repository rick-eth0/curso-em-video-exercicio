nota1 = float(input('primeira nota:'))
nota2 = float(input('segundo nota:'))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno esta em \033[1;32mRECUPERAÇÃO.\033[m')
elif media < 5:
    print('o aluno esta \033[1;31mREPROVADO.\033[m')
elif media >= 7:
    print('O aluno esta \033[1;34mAPROVADO.\033[m')