n = float(input('Digite um valor(m): '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
c = n * 100
mm = n * 1000
print('A medida de {}m corresponde a: '.format(n))
print('{:.3f} Km'.format(km))
print('{:.2f} hm'.format(hm))
print('{:.1f} dam'.format(dam))
print('{} dm'.format(dm))
print('{} cm'.format(c))
print('{} mm'.format(mm))
