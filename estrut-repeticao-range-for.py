for x in range(0,11):
    print(x, type(x)) #Por padrão, o end é \n, quebrando a linha.

print() #Pula 1 linha.

for y in range(0,11):
    print(y, end=" ") #O end no final cria um espaço depois de cada Y impresso.

print() 

#Exemplo usando a função built-in Range:
for tabuada in range(0, 51, 5):
    print(tabuada, end=", ")