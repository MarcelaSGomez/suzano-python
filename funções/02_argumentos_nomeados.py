def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso: {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Land Rover", "Commander", 2025, "ABC-1234")
salvar_carro(marca = "Land Rover", modelo = "Commander", ano = 2025, placa = "ABC-1234") #Argumentos nomeados
salvar_carro(**{"marca": "Land Rover", "modelo": "Commander", "ano": "2025", "placa": "ABC-1234"})