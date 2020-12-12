d = float(input('Qual a distancia sera percorrida em Km: '))
c = d * 0.50
l = d * 0.45
print(c)
print(l)
if d <= 200:
    print('O valor de sua passagem é de R${:.2f} '.format(c))
else:
    print('O valor de sua passagem é de R${:.2f}'.format(l))
