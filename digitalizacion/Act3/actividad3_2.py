#Diccionario para los dias de la semana.
dias_semana = {
    "Lunes": "90%",
    "Martes": "100%",
    "Miercoles": "100%",
    "Jueves": "100%",
    "Viernes": "100%",
    "Sabado": "80%",
    "Domingo": "80%"
}

#Mostrar los dias y sus %.
print("Dias de la semana y su porcentaje de trabajo:")
for dia, porcentaje in dias_semana.items():
    print(f"- {dia}")

#Pedir al usuario el dia.
dia_usuario = input("\nIntroduce un dia de la semana: ")

#Buscar en el diccionario.
if dia_usuario in dias_semana:
    print(f"El porcentaje de trabajo para {dia_usuario} es: {dias_semana[dia_usuario]}")
else:
    print("Dia no encontrado.")

