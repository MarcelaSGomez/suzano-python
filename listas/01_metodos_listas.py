#.append()
lista = []
lista.append(1)
lista.append("python")
lista.append([10,20,30])
print(lista)
print(' ')

#.copy()
lista2 = lista.copy()
print(lista2)
lista2[0] = "Troca o 1º elemento"
print(lista2)
print(' ')

#.clear()
print(lista.clear())
print(' ') #retorna None

#.count()
cor = ["vermelho", "azul", "verde", "azul"]
print(cor.count("azul"))
print(' ')

#.extend()
cor.extend("laranja")
cor.extend(["laranja"])
print(cor)
print(' ')

#.index()
print(cor.index("vermelho"))
print(cor.index("azul"))
print(cor.index("verde"))
print(cor.index("laranja"))
print(cor.index("l"))
print(' ')

#.pop()
linguagens = ["pyton", "js", "c", "java script", "c sharp"]
print(linguagens.pop())
print(linguagens.pop(1))
print(linguagens)
print(' ')

#.remove()
linguagens = ["pyton", "js", "c", "java script", "c sharp"]
linguagens.remove("js")
print(linguagens)
print(' ')

#.reverse()
linguagens = ["python", "js", "c", "java script", "csharp"]
linguagens.reverse()
print(linguagens)
print(' ')

#.sort
linguagens.sort() #Ordem alfabética
print(linguagens)
linguagens.sort(reverse=True) #Inverte a ordem
print(linguagens)
linguagens.sort(key=lambda x:len(x)) #Por tamanho da string.
print(linguagens)
linguagens.sort(key=lambda x:len(x), reverse=True) #Por tamanho da string.
print(linguagens)
print(' ')

#len()
print(len(linguagens))
print(' ')

#sorted()
print(sorted(linguagens))
print(sorted(linguagens, key=lambda x:len(x)))
print(sorted(linguagens, key=lambda x:len(x), reverse = True))

#Usando .count() com .index() para listar todas as posições de 1 elemento que se repete.
cores = ["vermelho", "azul", "azul"]

# Conta quantas vezes "azul" aparece
quantidade = cores.count("azul")

# Lista para armazenar as posições encontradas
posicoes = []

# Variável de controle para buscar as próximas ocorrências
indice = -1

for i in range(quantidade):
    # Procura o próximo "azul" depois do último índice encontrado
    indice = cores.index("azul", indice + 1)
    posicoes.append(indice)

print("Posições de 'azul':", posicoes)

#Usando .numerate() com .index() para listar todas as posições de 1 elemento que se repete.

cores = ["vermelho", "azul", "azul", "verde", "azul"]
posicoes = []

for i, cor in enumerate(cores):
    if cor == "azul":
        posicoes.append(i)

print("Posições de 'azul':", posicoes)






