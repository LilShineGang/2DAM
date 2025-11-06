import random   # Para simular el nivel de ruido
import time     # Para pausas entre lecturas

# Función que simula la lectura de ruido en decibelios (dB)
def leer_ruido():
    # Nivel base: 40 dB (habitación tranquila)
    # Variación aleatoria entre -5 y +40 dB
    ruido = 40 + random.uniform(-5, 40)
    return ruido

# Función que procesa el dato y detecta si se supera el umbral
def procesar_ruido(ruido, umbral=70):
    alertas = []
    if ruido > umbral:
        alertas.append(f"Ruido excesivo detectado: {ruido:.1f} dB")
    return alertas

# Función que simula realizar una llamada al dueño
def llamar_dueno(alertas):
    print("Llamando al dueño del piso...")
    for alerta in alertas:
        print("  → Mensaje:", alerta)

# Simulación del sistema
print("Iniciando sistema de monitoreo de ruido para Airbnb...\n")

for i in range(15):  # Simular 15 lecturas
    ruido = leer_ruido()
    print(f"Lectura {i+1}: Ruido={ruido:.1f} dB")

    alertas = procesar_ruido(ruido)

    if alertas:
        llamar_dueno(alertas)

    time.sleep(1)  # Pausa de 1 segundo entre lecturas
