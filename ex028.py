from random import randint
from time import sleep
o = randint(0, 5)
print('_-_'*20)
n = int(input('Adivinhe o número q estou pensando entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
print('                      Acertou' if o == n else '                               Errou')
print('O número que pensei foi {} !'.format(o))
print('=-'*20)
