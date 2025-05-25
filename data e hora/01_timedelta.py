from datetime import date, datetime, timedelta, time

tipo_carro = "P" #P, M ou G
tempo_p = 30
tempo_m = 45
tempo_g = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes = tempo_p)
    print(f"Horário de entrada: {data_atual} \nHorário de saída: {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes = tempo_m)
else:
    data_estimada = data_atual + timedelta(minutes = tempo_g)

    #timedelta pode receber atributos de dias, horas, segundos, minutos, semanas...

print(date.today()-timedelta(days=1))

print(datetime(2023,5,23,10,58) - timedelta(hours=1))
#Aqui mostra data e hora. Se quiser só hora, faz assim:

resultado = datetime(2023,5,23,10,58) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())
#Aqui eu consigo pegar só a data.