nome = str(input('Qual seu nome completo? ')).strip()
print('Analisando seu nome... ')
print('Seu nome em letras maiusculas é: {} .'.format(nome.upper()))
print('Seu nome em letras maiusculas é: {} .'.format(nome.lower()))
print('Seu nome tem o total de {} letras.'.format(len(nome)-nome.count(' ')))
