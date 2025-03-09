dias = int(input('Por quantos dias foi alugado o carro? '))
km = float(input('Quantos km foi rodado com o carro? '))

valortotal = (dias * 60) + (km * 0.15)

print('O total a pagar é R$ {:.2f}'.format(valortotal))