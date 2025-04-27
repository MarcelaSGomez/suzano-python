conta_normal = True
conta_universitaria = False
# Como conta_normal é True, ele imprime "Conta normal." e nem chega a testar o elif conta_universitaria. Eu só precisei definir False e True para que o código entenda que essas variáveis existem e possa seguir com a execução do próprio. Se trocar, ele vai considerar que está analisando uma conta universitária. E se forem as 2 falsas, ele vai rodar o código, mas não vai imprimir nada na tela, a menos que eu escreva um else no final com a seguinte mensagem: "Não foi possível identificar o seu tipo de conta".

saldo = 2000
saque = 4500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado.")
    elif saque <= (saldo + cheque_especial):
        print ("Saque realizado com cheque especial.")
    else:
        print("Saldo insuficiente.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado.")
    else:
        print("Saldo insuficiente.")

#Esse exercício seria melhor escrito, perguntando ao usuário o seu tipo de conta.