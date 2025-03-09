medida1 = float(input('Digite o comprimento da sua parede: '))
medida2 = float(input('Digite a altura da sua parede: '))

metroquadrado = medida1 * medida2
tintatotal = metroquadrado / 2

print('A metragem quadrada da sua parede é {:.2f} m²'.format(metroquadrado))
print('Para pintar sua parede de {:.2f} m² é necessário {:.2f} litros de tinta'.format(metroquadrado, tintatotal))