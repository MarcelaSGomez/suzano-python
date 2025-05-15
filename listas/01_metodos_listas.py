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

