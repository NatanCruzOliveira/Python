real = float(input('Quanto dinheiro você tem na carteira? R$ '))

dolar = real / 5.70

print('Com R${:.2f} você pode comprar US$ {:.2f} dolares'.format(real, dolar))