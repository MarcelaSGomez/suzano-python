salario = 2000

def salario_bonus (bonus):
    global salario #se não declarar essa linha, o interpretador vai dar erro., porque a variável foi declarada fora da função.
    salario += bonus
    return salario #Qdo uso return, o valor apresentado é guardado para uso futuro. Se usar print, ele surge na tela, mas é "esquecido" em seguida.

novo_salario = salario_bonus(500)
print(f"O salário com bonus é de R${novo_salario}.")