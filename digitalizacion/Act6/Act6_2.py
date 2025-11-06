import re
import time

# Diferencia entre re.match() y re.search():
# re.match() busca solo coincidencias al inicio del texto.
# re.search() busca coincidencias en cualquier parte del texto.
# En este ejemplo usamos re.search() porque el número (como 31.7) aparece en medio del mensaje, no al principio.

mensajes_sensor = [
    "Sensor1 -> temperatura=22.5ºC",
    "Sensor1 -> temperatura=18.1ºC",
    "Sensor1 -> temperatura=28.0ºC",
    "Sensor1 -> temperatura=30.0ºC",  # alerta: justo 30.0
    "Sensor1 -> temperatura=30.7ºC",  # alerta
    "Sensor1 -> temperatura=25.6ºC",
    "Sensor1 -> temperatura=33.5ºC",  # alerta
    "Sensor1 -> temperatura=24.8ºC",
    "Sensor1 -> temperatura=50.0ºC",  # límite superior 
    "Sensor1 -> temperatura=51.8ºC",  # máxima alerta
    "Sensor1 -> temperatura=60.0ºC"   # máxima alerta (límite)
]

print("Monitorizando datos IoT...\n")

for mensaje in mensajes_sensor:
    print(f"Recibido: {mensaje}")

    # Comprobamos el formato:
    if re.search(r"3[0-9]\.[0-9]", mensaje):
        print("→ Formato correcto detectado (rango 30.x - 39.x)")

    # Buscamos cualquier número con un decimal
    coincidencia = re.search(r"\d+\.\d", mensaje)
    if coincidencia:
        temperatura = float(coincidencia.group())

        # Diferenciamos los tres rangos
        if 50.0 < temperatura <= 60.0:
            print(f"\033[31m¡Máxima Alerta! Temperatura superior a 50.0 ºC ({temperatura}ºC).\033[0m\n")
        elif 30.0 <= temperatura <= 50.0:
            print(f"\033[33mAlerta. Temperatura superior o igual a 30.0 ºC ({temperatura}ºC).\033[0m\n")
        else:
            print(f"Temperatura normal ({temperatura}ºC).\n")
    else:
        print("Formato de lectura incorrecto: no se ha detectado un valor con decimal.\n")

    time.sleep(1)

