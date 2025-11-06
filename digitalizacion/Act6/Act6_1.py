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
    "Sensor1 -> temperatura=24.8ºC"
]

print("Monitorizando datos IoT...\n")

for mensaje in mensajes_sensor:
    print(f"Recibido: {mensaje}")

    # Patrón: busca números de 30.0 a 39.9 (dos cifras y un decimal)
    # 3[0-9]\.[0-9] -> empieza por 3, sigue un dígito (0–9), un punto y otro dígito (0–9)
    if re.search(r"3[0-9]\.[0-9]", mensaje):
        print("\033[31m¡Alerta! Temperatura superior o igual a 30.0 ºC detectada.\033[0m\n")
    else:
        print("Temperatura normal.\n")

    time.sleep(1)
