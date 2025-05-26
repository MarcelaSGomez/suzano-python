from datetime import datetime

print("Bem-vindo ao Banco Marcela S.A. Escolha uma opção no Menu abaixo.")
print(" ")
menu = ("""Menu:
    (d) Depósito
    (s) Saque
    (q) Sair
      
    Opção Escolhida: """)

saldo = 0
data_transacao = datetime.now()

while True:
    opcao = str(input(menu))

#Depósito
    if opcao == "d":
        valor = float(input("Digite o valor do Depósito: R$ "))
        
        if valor > 0:
            saldo =+ valor
            print(f"Depósito: R${valor:.2f}")
            data_transacao =+ datetime.today()

            if data_transacao >
        
        else:
            print("Operação falhou. O valor digitado é inválido.")

#Saque
    if opcao == "d":
        valor = float(input("Digite o valor do Saque: R$ "))
        
        if valor > 0:
            saldo =- valor
            data_transacao =+ datetime.today()
            print(f"Saque: R${valor:.2f}")
        
        else:
            print("Operação falhou. O valor digitado é inválido.")
