nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

print(nome, idade) #Por padrão, o end é quebra de linha. Por isso o 2º print já foi na linha abaixo.
print(nome, idade, end="...") #Sem o \n, o próximo print vem na mesma linha.
print(nome, idade, end="...\n") 
print(nome, idade, sep="@") #Sep é o reparados entre as 2 variáveis. O sep padrão é 1 espaço, como visto no 1º print.
print(nome,idade, sep="#", end="!\n") #Posso acumular argumentos.