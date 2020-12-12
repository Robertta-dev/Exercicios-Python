s = float(input('Qual o salário do funcionario? R$ '))
a = s + (s*15/100)
print('O salário de R${:.2f},com reajuste de 15%, ficará R${:.2f}'.format(s, a))

