opcao = -1

while opcao != 0:
    opcao = int(input("[1]Saque [2]Extrato [0]Sair \nDigite a opção escolhida: "))
    if opcao == 1:
        print("Sacando... ")
    elif opcao == 2:
        print("Exibindo extrato... ")
else:
    print("Obrigado por usar nosso sistema bancário.")
