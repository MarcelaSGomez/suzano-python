nome = "Marcela"
mensagem = f"""
    Olá, meu nome é {nome}.
        Eu estudo Python.
E essa mensagem tem vários recuos diferentes.
"""

print(mensagem)

mensagem2 = f'''
Olá, meu nome é {nome}.
Eu estudo Python.
E essa mensagem tem vários recuos diferentes.
'''
print(mensagem2)

#Criando um menu dentro de 1 print só com string de múltiplas linhas.
print("""
    ========= MENU =========
    
    1 - Depositar
    2 - Sacar
    0 - Sair
    ========================
      
      Obrigado por usar nosso sistema!
      """)

print("========= MENU =========") #A forma mais complexa para criar o mesmo menu.
print("")
print("1 - Depositar \n2 - Sacar \n0 - Sair")