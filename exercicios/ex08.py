medida = float(input('Ama distancia em metros: '))
cm = medida * 100
mm =medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m  corresponde a \n{:.0f}cm e \n{:.0f}mm e \n{}dm \n{}dam \n{}hm \n{}km'.format(medida, cm, mm, dm, dam, hm, km))

