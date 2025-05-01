while True:
    numero = int(input("Informe um número: "))
    
    if numero == 10: #Ao digitar 10, o programa para.
        break
    
    if numero % 2 == 0: #Se não é 10, segue com o programa. Se o número for par, o programa não    escreve na tela. Se for impar, escreve. Nos 2 casos, o loop recomeça.
        continue

    print (numero)

