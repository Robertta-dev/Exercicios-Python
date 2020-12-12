n = str(input('Qual seu nome? ')).strip()
s = n.split()
n1 = s[0]
n2 = s[len(s)-1]
print('Prazer em te conhecer, {} {}!'.format(s[0], s[len(s)-1]))
print('O primeiro nome é: {}'.format(s[0]))
print('O seu ultimo nome é {}'.format(s[len(s)-1]))
