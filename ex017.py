import math
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
h2 = (co ** 2 + ca ** 2)**(1/2)
hip = math.hypot(ca, co)
print('O valor da hipotenusa é: {:.2f} '.format(h2))
print('Hipotenusa: {}'.format(math.sqrt(h2)**2))
print('exemplo 2: {}'.format(math.hypot(ca, co)))
print('exemplo 3: {} '.format(hip))
#h2 = ca2 + co2