texto = input("Informe uma palavra: ")
VOGAIS = "AEIOU"

for letra in texto: 
    if letra.upper() in VOGAIS: 
        print(letra, end=" ") 

print() #Garante uma quegra de linha a cada loop.

#Ao usar o FOR, o python automaticamente entende que a variável letra irá se tornar a representação temporária de cada caractere da string enquanto o laço está em execução.
#Ao usar o .upper() o programa transforma todas as letras de texto (que o usuário inseriu) em maiúsculas, então não ignora o caractere, caso esteja em minúscula. É para que não haja erro na resposta. Mas não deixa tudo maiúsculo no final.
#O end garante que sempre haja um espaço depois de cada caractere que vai entrar na resposta.