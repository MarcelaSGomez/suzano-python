#IN e NOT IN - Usado spara verificar se um objeto está numa sequência

frutas = ["laranja", "uva", "limão"]
print("limão" in frutas)
print("uva" not in frutas)

curso = "Curso de Python"
print("y" in curso) #Qualquer caractere que esteja dentro da string é True.
print("Python" in curso) #Parte da sequência também é True.
print ("so de" in curso) #Parte da sequência também é True.
print("python" in curso) #Se tiver alguma diferença dentro da sequência, dará False. p minúsculo. Maiúsculas e Minúsculas contam.
print("X" not in curso) #Letras que não fazem parte da string serão False.
