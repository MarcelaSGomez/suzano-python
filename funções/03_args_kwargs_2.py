def cadastro(**kwargs):
    print("Cadastro:")
    for chave,valor in kwargs.items():
        print(f"{chave.capitalize()}: {valor}")
        
cadastro(nome="Lucas", idade=30, cidade="Recife")
print("------------------------------")

#Exemplo com *args e *kwargs

def exibir_poema(data, titulo, *args, **kwargs):
    texto = "\n".join(args) #Quebra de linha a cada item do args
    dados_finais = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data}\n\n{titulo}\n\n{texto}\n\n{dados_finais}"
    print (mensagem)

exibir_poema ("Sexta-feira, 09 de Maio de 2025", #1ª linha é identificada como data
              "Segue o teu destino".upper(), #2ª linha é identificada como titulo
              "Segue o teu destino,", # #3ª linha em diante separadas por vígula são identificadas como args (tuplas)
              "Rega as tuas plantas,",
              "Ama as tuas rosas.",
              "O resto é a sombra",
              "De árvores alheias.",
              autor="Fernando Pessoa", #Quando começa o mapeamento chave=valor ele entende que é kwargs (dicionario)
              ano="1916")