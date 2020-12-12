import math
a = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('Através do ângulo informado obtivemos os valores: \nSen {:.2f}  \nCos {:.2f}  \nTan {:.2f}'.format(sen, cos, tan))
