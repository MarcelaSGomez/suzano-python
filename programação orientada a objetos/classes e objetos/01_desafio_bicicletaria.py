class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
#O método __str__ é um método especial do Python (chamado "dunder method", de double underscore). Ele define como um objeto será representado em forma de string quando for usado, por exemplo, em: print(objeto) ou  str(objeto). Se você não definir o __str__, o Python usa uma representação padrão (como <__main__.Bicicleta object at 0x000001A3D...>), que mostra o tipo e o endereço de memória do objeto. 
 
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()