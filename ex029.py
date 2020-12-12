from time import sleep
v = float(input('Qual a velocidade do veiculo (Km/h): '))
m = (v - 80) * 7.00
print('ANALISANDO...')
sleep(3)
if v <= 80:
    print("Velocidade Permitida!")
else:
    print('Você ultrapassou a velocidade permitida!!!')
    print('Valor da multa R${:.2f} !'.format(m))
