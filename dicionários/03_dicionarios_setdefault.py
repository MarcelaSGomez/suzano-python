contatos = {
    "marcela@gmail.com": {"nome": "Marcela", "telefone": "123"},
    "ale@gmail.com": {"nome": "Ale", "telefone": "456"},
    "rafa@gmail.com": {"nome": "Rafa", "telefone": "789", "extra": {"a": 1}}
}

contatos.setdefault("gabi@gmail.com", {"nome": "Gabi", "telefone": "101"})
print (contatos)