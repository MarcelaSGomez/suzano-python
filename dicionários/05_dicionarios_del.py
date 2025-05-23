contatos = {
    "marcela@gmail.com": {"nome": "Marcela", "telefone": "123"},
    "ale@gmail.com": {"nome": "Ale", "telefone": "456"},
    "rafa@gmail.com": {"nome": "Rafa", "telefone": "789", "extra": {"a": 1}}
}

del contatos["marcela@gmail.com"]["telefone"]
del contatos["rafa@gmail.com"]
#del contatos - apaga o dicionário todo.

print(contatos)