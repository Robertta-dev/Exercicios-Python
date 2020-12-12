frase = ('  Que dia lindo para aprender programação  ')
print(frase.split())
print('-'.join(frase))
doc = ("""-	Cópia da carteira de identidade e do CPF;
-	Comprovante de renda;
-	Cópia comprovante de residência (água ou luz);
-	Cópia da certidão de casamento;""")
print(doc)
print(len(doc))
doc = doc.replace('renda','salário')
print(frase.split())
print(doc.count('r'))