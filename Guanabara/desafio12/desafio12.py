preco = float(input('Qual é o preço do produto? R$ '))
desconto = float(input('Qual é o percentual de desconto do profuto? '))

novopreco = preco * (1 - (desconto / 100))

print('O produto que custava R$ {:.2f} na promoção de {:.2f} % vai custar R$ {:.2f}'.format(preco, desconto, novopreco))
