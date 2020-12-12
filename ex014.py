c = float(input('Informe a temperatura: C° '))
f = c * 9/5 + 32
k = c + 273.15
print(c)
print(f)
print(k)
print('A temperatura {:.1f}C°, convertida resulta em:'.format(c))
print('{:.2f} F°'.format(f))
print('{:.2f} kelvin'.format(k))
