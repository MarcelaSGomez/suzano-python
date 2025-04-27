nome = 'Marcela'
idade = 39
nome = 'Gabriela' # O Python automaticamente descarta o valor Marcela e printa o novo valor.

nome, idade = "Marcela", 39 # Posso escrver várias variáveis em 1 linha, só preciso separar com vírgula e usar "" em strings.
nome, idade = ("Marcela", 39) # O uso de () é opcional.

print (nome, idade)

a = "nome" # evitar, pois a não siginifica nada em referência futura.
saque_limite_diario = 1000 # a viriável fica bem clara para manutenção futura.
ESTADOS_BRASILEIROS = ['SP', 'RJ', 'SC', 'CE'] # Por convenção, qualquer programador vai ler esse código e entender que é uma Constante. Mas se ele mudar o valor (por ex.: ESTADOS_BRASILEIROS = 10) o python vai mudar o valor da variável.

print (a, saque_limite_diario, ESTADOS_BRASILEIROS)