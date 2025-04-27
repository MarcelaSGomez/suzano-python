# AND - Para ser True, tudo deve ser True.
# OR - Para ser True, basta um ser True.

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print (False or False)

#Exercício: O cliente só pode sacar se tiver saldo acima ou igual do valor do saque e o valor do saque menor ou igual ao limite. Exceto quando a conta for especial. Nesse caso, o saque tem que ser inferior ou igual ao saldo.
saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)) #Mesmo resultado, mas de forma melhor organizada. O parêntesis pode mudar resultado, pois interfere na ordem de precedência.

#Outra forma de resolver esse exercício, facilitando a leitura e a linha de raciocínio é:

conta_padrao_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
pode_sacar = conta_padrao_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print (pode_sacar)