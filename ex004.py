n =str(input('Digite algo: '))
print(type(n))
print('Numérico?' , {n.isnumeric()})
print('Letras?',{n.isalpha()})
print('MAIUSCULA?',{n.isupper()})
print('MINUSCULA?',{n.islower()})
print('Pode imprimir?',{n.isprintable()})
print('É titulo?',{n.istitle()})
print('É um espaço?',{n.isspace()})
print('É decimal?',{n.isdecimal()})
