nome = "mArCeLa"

print(nome.upper())
print(nome.lower())
print(nome.title()) 

texto = "  Olá, Mundo   "

print(texto + "!")
print(texto.strip() + "!")
print(texto.lstrip() + "!")
print(texto.rstrip() + "!")
print(texto,"!") #Qdo uso a vírgula entre as strings, ela acrescenta um espaço. Ao usar o +, não acrescenta espaço. Ele entra logo depois da primeira string.

menu = "Python"

print("####" + menu + "####")
print(menu.center(14,"#")) #Forma mais simples de fazer o comando acima. Se alterar o conteúdo da variável menu, ele automaticamente ajusta para ficar 14 caracteres e a variável no centro.
print(menu.center(14)+".")
print("P-y-t-h-o-n")
print("-".join(menu))

menu = "Python"
for x in menu:
    print(x,end="-") #Tb faz a iteração, mas até o último caractere da lista.

#A forma de criar o mesmo resultado com for é:
menu = "Python"
for i in range(len(menu)): 
    if i < len(menu) - 1:
        print(menu[i], end="-")
    else:
        print(menu[i])

#Len - função do Python que retorna o tamanho (ou seja, o número de elementos) de algo.            len(menu) é 6 — ou seja, a quantidade de letras na string "Python".
#menu[i] acessa o caractere que está na posição i da string menu. Lembre que as posições começam em 0, não em 1!