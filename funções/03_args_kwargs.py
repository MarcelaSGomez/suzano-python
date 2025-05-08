#args
#Nesse primeiro código, a função é chamada e imprime apenas a tupla e o resultado da soma. Não houve um retornol, pois não pedi o print(somar(1,2,3,4)). Então os resultados dos 2 primeiros prints não podem ser usados depois.
def somar(*args):
    print(args) 
    print(sum(args))

somar(1,2,3,4)

#Nesse 2º código, os resultados são: 1º o print da tupla e depois o retorno da função. O retorno pode ser armazenado numa variável e usado depois.

def somar(*args):
    print(args)
    return(sum(args))

print(somar(1,2,3,4))

#Aqui, armazenei o retorno na variável resultado.
def somar(*args):
    print(args)
    return(sum(args))

resultado = somar(1,2,3,4)
print(resultado)

#kwargs

#Nste exercício temos um exemplo para entender o método .items()
dicionario = {"nome": "João", "idade": 30, "cidade": "Lisboa"}

for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")


#Neste exercício, usamos o kwargs:
def mostrar_informacoes(**kwargs):
    print(kwargs)           # Mostra o dicionário
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_informacoes(nome="Ana", idade=25, cidade="Fortaleza")

#Inventei esse exercício para entender melhor:
def menu(**cardapio):
    print(cardapio)
    for chave, valor in cardapio.items():
        print(f"{chave}: {valor}")

menu(prato="Espaguete", preco=25.90)
