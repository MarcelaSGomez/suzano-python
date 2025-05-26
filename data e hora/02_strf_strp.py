import datetime
d = datetime.datetime.now()
print(d.strftime("%d/%m/%Y %H:%M")) #Formatando Data e Hora(:%S - para incluir segundos)

date_string = "16/03/2020 10:00" #Convertendo String para Datetime
d=datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")

#Diferentes formas de formatar data e hora:
#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

print(" ")

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_string = "2025-10-20 15:30"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

print(" ")

data_convertida = datetime.strptime(data_hora_string, mascara_en)
print(data_convertida)
print(type(data_convertida))
print(data_convertida.strftime("%Y"))

 