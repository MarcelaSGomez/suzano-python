contatos = {
    "marcela@gmail.com": {"nome": "Marcela", "telefone": "123"},
    "ale@gmail.com": {"nome": "Ale", "telefone": "456"},
    "rafa@gmail.com": {"nome": "Rafa", "telefone": "789", "extra": {"a": 1}}
}

resultado1 = contatos.pop("ale@gmail.com")
print(resultado1)

resultado2 = contatos.pop("gabi@gmail.com", "não encontrado")
print(resultado2)

print(contatos)
