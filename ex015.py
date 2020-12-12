import math
d = int(input('Quantos dias o carro foi alugado? '))
k = float(input('Quantos Km rodados? '))
t = (d * 60) + (k * 0.15)
print('O valor total a ser pago é R${:.2f} R${:.2f}'.format(t, math.ceil(t)))
# o arredondamento não era necessário, foi apenas teste do import