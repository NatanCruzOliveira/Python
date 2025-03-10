from math import sqrt

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hip = sqrt(co**2 + ca**2)

print('A partir dos catetos, a soma da hipotenusa é {:.2f}'.format(hip))
