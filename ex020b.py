import random
a1 = input('Informe o nome do primeiro aluno: ')
a2 = input('Informe o nome do segundo aluno: ')
a3 = input('Informe o nome do terceiro aluno: ')
a4 = input('Informe o nome do quarto aluno: ')
alunos = [a1, a2, a3, a4]
r = random.sample(alunos, 4)
print('A ordem que as apresentações ocorrerão sera: \n{}'.format(r))
#erro print('A ordem que as apresentações ocorrerão sera: \n{}'.format(alunos))