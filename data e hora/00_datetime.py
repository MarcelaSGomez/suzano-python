from datetime import date #Aqui, estamos importando a classe date de dentro do módulo datetime. Isso permite usar date(...) diretamente para criar um objeto de data.
#Tb poderia escrever: from datetime import date, datetime, time. E fazer tudo junto.

data = date(2025, 5, 20) #Essa função cria uma data sem horário (só a data mesmo). E o valor é guardado na variávle data.
print(data) 
print(date.today())


from datetime import datetime #Tb poderia escrever: from datetime import date, datetime. E fazer tudo junto.
data_hora = datetime (2025, 5, 23, 9,53,20)
print(data_hora)
print(datetime.today())

from datetime import time
hora = time(9,59,13)
print(hora)