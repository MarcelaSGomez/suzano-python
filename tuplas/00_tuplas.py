frutas = ("laranja", "pera", "uva",)
print(frutas[0])
print(frutas[-1])

#fatiamento
tupla = ("p","y","t","h","o","n",)
print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

#Não suporta atrbuições de itens. Quer dizer que não posso alterar os dados de uma tupla.
#tupla[0] = "P"
#TypeError: 'tuple' object does not support item assignment

#Iterar tuplas - FOR
carros = ("gol", "celta", "palio",)
for carro in carros:
    print(carro)

#Índice em tuplas - Enumerate
carros = ("gol", "celta", "palio",)
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#Is instance
carros = ("gol",)
print(isinstance(carros, tuple))
#isinstance() é uma função embutida do Python usada para verificar se um objeto pertence a um determinado tipo (ou classe). É true porque te4m a virgula no final. Sem ela, seria uma string.