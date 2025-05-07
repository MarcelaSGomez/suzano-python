nome = "Marcela"
idade = 39
profissao = "Programadora"
linguagem = "Python"
saldo = 45.345

dados = {"nome": "Marcela", "idade": 39} #dicionário

print("nome: %s \nidade: %d" %(nome, idade)) #Old Style. Não se usa mais!
print("nome: {} idade: {} nome: {}".format(nome, idade, nome)) #Format simples
print("nome: {0} idade: {1} nome: {0}".format(nome, idade)) #Format com índice
print("nome: {name} idade: {age}".format(age=idade, name=nome)) #Format criando nomes para as chaves
print("nome: {nome} idade: {idade}".format(**dados)) #Format com dicionário
print(f"nome: {nome} idade: {idade} saldo: R${saldo:.2f}") #F-string exemplo 1
print(f"nome: {nome} idade: {idade} saldo: R${saldo:*>10.2f}") #F-string exemplo 2
