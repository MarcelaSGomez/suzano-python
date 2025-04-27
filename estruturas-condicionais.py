MAIOR_IDADE = 18
IDADE_ESPECIAL = 17 #Fictício

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade. Pode tirar a CNH.")

elif idade == IDADE_ESPECIAL:
    print("Você pode fazer aulas teóricas, mas não práticas.")

else:
    print("Você é menor de idade. Ainda não pode ter CHN.")