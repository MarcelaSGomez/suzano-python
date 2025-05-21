numeros = {1,2,3,2}

numeros = list(numeros) #Primeiro transforma em lista para poder acessar os itens do conjunto.
print(numeros[0:3]) #Ele já ignora o segundo 2, pois em conjuntos não há itens duplicados.

carros = {"palio", "gol", "palio", "celta"}
for carro in carros:
    print(carro)
#gol
#palio
#celta

carros = {"palio", "gol", "palio", "celta"}
for indice, carro in enumerate(carros):
    print(f"{indice} - {carro}")
#0 - gol
#1 - celta
#2 - palio