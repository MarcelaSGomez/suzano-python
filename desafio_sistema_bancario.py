print("Bem-vindo ao Banco Marcela. Por favor, escolha uma opção do menu abaixo:")

menu = """\nMenu
    (d) Depositar
    (s) Sacar
    (e) Ver Extrato
    (q) Sair

    Opção Escolhida: """

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input (menu) #Recebe a resposta do usuário. É string.

    if opcao == "d":
        valor = float(input("\nInforme o valor do depósito: R$ ")) #salvo o deposito na variável valor
        
        if valor > 0:
            saldo += valor #Adiciono o depósito na variável saldo.
            extrato += f"Depósito: R${valor:.2f}\n" #Começo a compor meu extrato.

        else:
            print("Operação falhou. O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("\nInforme o valor do saque: R$ "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou. Você não tem saldo suficiente.")
    
        elif excedeu_limite:
            print("Operação falhou. O saque solicitado excede o limite permitido.")
    
        elif excedeu_saques:
            print("Operação falhou. Você já atingiu o limite máximo de saques diários.")
    
        elif valor > 0:
            saldo -= valor #Atualizo o valor do saldo, agora com saque.
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1 #Atualizo o nº de saques realizados.

        else:
            print("Operação falhou. O valor informado é inválido.")

    elif opcao == "e":
        print("\n******EXTRATO BANCÁRIO******")
        print("Não foram realizadas movimentações." if not extrato else extrato) #if not extrato - se extrato estiver vazio, digite a frase anterior. Se não estiver vazio, siga para a próxima linha do bloco de comandos.
        print(f"Saldo Atual: R${saldo:.2f}")
        print("\n***Fim do Extrato bancário***")
    
    elif opcao == "q":
        break

    else:
        print("Seleção inválida. Por favor, escolha 1 das opções válidas.")