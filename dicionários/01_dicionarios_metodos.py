#Método - .keys
contatos = {
    "marcela@gmail.com": {"nome": "Marcela", "telefone": "123"},
    "ale@gmail.com": {"nome": "Ale", "telefone": "456"},
    "rafa@gmail.com": {"nome": "Rafa", "telefone": "789", "extra": {"a": 1}}
}

print(contatos.keys())
print(' ')

#Método .items()
dados_usuario = {}

# Coletando informações do usuário
dados_usuario["nome"] = input("Digite seu nome: ")
dados_usuario["idade"] = input("Digite sua idade: ")
dados_usuario["cidade"] = input("Digite sua cidade: ")

# Exibindo os dados com .items()
print("\nDados informados:")
for chave, valor in dados_usuario.items():
    print(f"{chave.capitalize()}: {valor}")

