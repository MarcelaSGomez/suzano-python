from datetime import datetime, timedelta, timezone
#datetime: classe usada para trabalhar com data e hora completas.
#timedelta: representa diferenças de tempo (ex: 2 horas, 15 minutos etc.).
#timezone: classe usada para definir um fuso horário fixo.

dataoslo = datetime.now(timezone(timedelta(hours=2))) #configura o horário de Oslo que é GMT+2
datasp = datetime.now(timezone(timedelta(hours=-3)))
#configura o horário de São Paulo que é GMT-3

print(dataoslo)
print(datasp)

#timedelta(hours=2) → cria uma diferença de tempo de 2 horas.

#timezone(timedelta(hours=2)) → cria um fuso horário UTC+2.

#datetime.now(timezone(...)) → pega a data e hora atual, mas no fuso horário UTC+2 (que é o de Oslo durante o horário de verão).