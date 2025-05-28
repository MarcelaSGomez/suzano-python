def calcular_saldo(transacoes):
    saldo = 0

    # Soma todas as transações (positivas e negativas)
    for transacao in transacoes:
        saldo += transacao

    # Retorna o saldo formatado com duas casas decimais e vírgula no lugar do ponto
    return f"R$ {saldo:.2f}".replace('.', ',')

# Pede ao usuário que digite os valores
entrada_usuario = input("Digite os valores das transações, separados por vírgula (ex: 1000, -200.50, 300): ")

# Remove espaços e tenta converter cada valor para float
entrada_usuario = entrada_usuario.replace(" ", "")

transacoes = []

# Processa cada valor digitado
for valor in entrada_usuario.split(","):
    try:
        transacoes.append(float(valor))
    except ValueError:
        print(f"Aviso: valor inválido ignorado → '{valor}'")

# Calcula o saldo e imprime o resultado
resultado = calcular_saldo(transacoes)
print("Saldo final:", resultado)
