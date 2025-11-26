import random  # Para simular valores de sensores
import time    # Para pausas entre lecturas

# Función que simula la lectura de sensores
def leer_sensores():
    temperatura = 20 + random.uniform(-2, 10)  # Temperatura base 20°C con variación [-2, +10]
    vibracion = 0.02 + random.uniform(-0.01, 0.1)  # Vibración base 0.02 g con variación [-0.01, +0.1]
    return temperatura, vibracion  # Retorna ambas lecturas

# Función que procesa datos localmente (Edge Computing)
def procesar_datos(temp, vib):
    alertas = []  # Lista para acumular alertas
    if temp > 25:  # Umbral de temperatura
        alertas.append(f"Temperatura alta detectada: {temp:.2f} ºC")
    if vib > 0.08:  # Umbral de vibración
        alertas.append(f"Vibración fuera de rango: {vib:.3f} g")
    return alertas  # Devuelve alertas (vacías si no hay problemas)

# Simulación del sistema
print("Iniciando sistema de monitoreo con Edge Computing...\n")

for i in range(10):  # Simular 10 lecturas
    temp, vib = leer_sensores()  # Obtener lectura de sensores
    print(f"Lectura {i+1}: Temp={temp:.2f}ºC, Vib={vib:.3f}g")

    # Procesar localmente en el "Edge"
    alertas = procesar_datos(temp, vib)

    # Enviar solo las alertas a la "nube" (aquí se imprime)
    if alertas:
        print(">> Enviando a la nube:", alertas)

    time.sleep(1)  # Esperar 1 segundo entre lecturas
