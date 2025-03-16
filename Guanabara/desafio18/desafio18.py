import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo {} tem o SENO de {:.3f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo {} tem o COSSENO de {:.3f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo {} tem a TANGENTE de {:.3f}'.format(angulo, tangente))
