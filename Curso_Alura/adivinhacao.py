print("*"*30)
print("Bem Vindes ao jogo!")
print("*"*30)
numero_secreto = 42
chute = input("Digite um número: ")
numero = int(chute)
acertou = numero == numero_secreto
menor = numero < numero_secreto
maior = numero > numero_secreto

    if (acertou):
       print("Acertou")
    else:
         if(menor):
              print("Errou! O seu número foi menor do que o número secreto!")
            elif(maior):
                print("Errou! O Seu número foi maior do que o número secreto!")

print("Você digitou o número...", chute)
print("o numero secreto é...", numero_secreto)

print("Fim de jogo!")
print("Tente novamente!!!")
