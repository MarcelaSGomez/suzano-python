pessoa = {"nome": "Guilherme", "idade": 28}
pessoa = dict (nome= "Guilherme", idade= 28) #igual
print(pessoa)
pessoa["telefone"] = "123-456"
print(pessoa)
pessoa["nome"] = "Maria"
print(pessoa)

#Dicionários aninhados

contatos = {
    "marcela@gmail.com": {"nome": "Marcela", "telefone": "123"},
    "ale@gmail.com": {"nome": "Ale", "telefone": "456"},
    "rafa@gmail.com": {"nome": "Rafa", "telefone": "789", "extra": {"a": 1}}
}

info = contatos["rafa@gmail.com"]["extra"]["a"]
print(info)

for chave in contatos:
    print(chave, contatos[chave])
    #Retorna o dicionário completo. Não é a melhor forma de acessar todos os itens.
print(' ')

for chave, valor in contatos.items():
    print(chave, valor)

#Entendendo objetos imutáveis
def modifica_valor(x):
    x = x + 10
    print("Dentro da função:", x)

a = 5
modifica_valor(a)
print("Fora da função:", a)

    