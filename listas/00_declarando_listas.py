frutas = ["laranja", "maçã", "uva"]
print(frutas)
fruta = [] #posso declarar uma lista vazia. Sem nenhum valor declarado.
print(fruta)
letras = list("python") #List exige um elemento iterável. Assim cada letra da string se torna um elemento da lista.
print(letras)
numeros = list(range(10)) #Cada elemento retornado da função range se torna um elemento da lista números.
print(numeros)
carro = ["Ferrari", "F8", 4200000.00, 2020, True] #Lista com elementos diferentes: string, float, inteiro, valor booleano.
print(carro)
print(" ")

frutas = ["laranja", "maçã", "uva"] 
print(frutas[1]) #Usando índice que começa em Zero, posso acessar elementos da lista.
print(frutas[-1]) #Índice negativo. Começa por -1, que é o último elemento da lista.
print(" ")

matriz = [       #Lista Aninhada: lista de listas. Índice de linhas e colunas.
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(" ")

linguagem = ['p', 'y', 't', 'h', 'o', 'n']
#             0    1    2    3    4    5
print(linguagem[2:]) # Começa no 2 e vai até o final, pois o mesmo não foi definido.
print(linguagem[:2]) # Começa no Zero, pois não foi definido, e termina no 2.
print(linguagem[1:3]) # Começa no 1 e termina no 2, pois o final é exclusivo.
print(linguagem[0:3:2]) #Começa no zero e termina no 3, mas pula 1 casa, imprimindo a cada 2 casas.
print(linguagem[::]) # Vazio. O default é começar no zero, terminar no fim e não pular.
print(linguagem[::-1]) # -1 Inverte a ordem, començando do fim.
print(" ")

carros = ["gol", "celta", "palio"] # iterar lista e também expor índice:
for carro in carros:
    print (carro)
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")