nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome, sep="_")
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade <= 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")
usuario = input("Informe o usuário do sistema: ")

if(usuario == "betta"):
    print("Seja bem-vinda, Betta!")
elif(usuario == "robertta"):
    print("Seja bem-vinda, Robertta!")
elif(usuario == "Cali"):
    print("Seja bem-vinda, Calíope!")
else:
    print("Usuário não identificado!")
# Seguem todas as operadores de comparação:
# < - menor que
# > - maior que
# <= - menor ou igual a
# >= - maior ou igual a
# == - igual a
# != - diferente de