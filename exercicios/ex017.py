import math
co = float(input('comprimento do cateto aposto: '))
ca = float(input('comprimento do cateto adiancnete: '))
hi = math.hypot(co, ca)
print('A hipetenusa vai medir {:.2f}'.format(hi))
