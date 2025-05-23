contatos = {
    "marcela@gmail.com": {"nome": "Marcela", "telefone": "123"},
    "ale@gmail.com": {"nome": "Ale", "telefone": "456"},
    "rafa@gmail.com": {"nome": "Rafa", "telefone": "789", "extra": {"a": 1}}
}

resposta1 = "marcela@gmail.com" in contatos
print(resposta1)

resposta2 = "marce@gmail.com" in contatos
print(resposta2)

resposta3 = "nome" in contatos["ale@gmail.com"] #busca dentro da chave que é um dicionário tb.
print(resposta3)