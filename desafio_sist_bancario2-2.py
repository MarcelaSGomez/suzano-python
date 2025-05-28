def calcular_saldo(transacoes):
    saldo = 0
    for transacao in transacoes:
        saldo += transacao
    return f"R$ {saldo:.2f}".replace('.', ',')

entrada_usuario = input("Digite os valores das transações, separados por vírgula (ex: 1000, -200.50, 300): ")

entrada_usuario = entrada_usuario.replace(" ", "")
valores = entrada_usuario.split(",")

# Aqui estamos assumindo que todos os valores são válidos
transacoes = [float(valor) for valor in valores]

resultado = calcular_saldo(transacoes)
print("Saldo final:", resultado)