v = float(input('Qual o valor do produto? R$ '))
vd = v * 5 / 100
d = v - vd
print('O valor do produto era de R${:.2f}, e com desconto de 5% fica por R${:.2f}'.format(v, d))
