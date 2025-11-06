'''
Fin de la pobreza: 1Fdlp 🡪r"^[0-9][A-Z][a-z]{3}$" o bien r"^\d[A-Z][a-z]{3}$"

Hambre cero: 2Hc 🡪 r"^\d[A-Z][a-z]$" o bien r"^[0-9][A-Z][a-z]$"

Salud y bienestar: 3Syb 🡪 r"^\d[A-Z][a-z]{2}$" o bien r"^[0-9][A-Z][a-z]{2}$"

Educación de calidad: 4Edc 🡪 r"^\d[A-Z][a-z]{2}$" o bien r"^[0-9][A-Z][a-z]{2}$"

Igualdad de género: 5Idg 🡪 r"^\d[A-Z][a-z]{2}$" o bien r"^[0-9][A-Z][a-z]{2}$"

Agua limpia y saneamiento: 6Alys 🡪 r"^\d[A-Z][a-z]{2}$" o bien r"^[0-9][A-Z][a-z]{2}$"

Energía asequible y no contaminante: 7Eaync 🡪 r"^\d[A-Z][a-z]{3}$" o bien r"^[0-9][A-Z][a-z]{3}$"

Trabajo decente y creciente económico: 8Tdyce 🡪 r"^\d[A-Z][a-z]{4}$" o bien r"^[0-9][A-Z][a-z]{4}$"

Industria, innovación e infraestructura: 9Iiei 🡪 r"^\d[A-Z][a-z]{3}$" o bien r"^[0-9][A-Z][a-z]{3}$"

Reducción de las desigualdades: 10Rdld 🡪 r"^\d{2}[A-Z][a-z]{3}$" o bien r"^[0-9]{2}[A-Z][a-z]{3}$"

Ciudades y comunidades sostenibles:11Cycs 🡪 r"^\d{2}[A-Z][a-z]{3}$" o bien r"^[0-9]{2}[A-Z][a-z]{3}$"

Producción y consumo responsables: 12Pycr 🡪 r"^\d{2}[A-Z][a-z]{3}$" o bien r"^[0-9]{2}[A-Z][a-z]{3}$"

Acción por el clima: 13Apec 🡪 r"^\d{2}[A-Z][a-z]{3}$" o bien r"^[0-9]{2}[A-Z][a-z]{3}$"

Vida submarina: 14Vs 🡪  r"^\d{2}[A-Z][a-z]$" o bien r"^[0-9]{2}[A-Z][a-z]$"

Vida de ecosistemas terrestres: 15Vdet 🡪 r"^\d{2}[A-Z][a-z]{3}$" o bien r"^[0-9]{2}[A-Z][a-z]{3}$"

Paz, justicia e instituciones sólidas: 16Pjeis 🡪 r"^\d{2}[A-Z][a-z]{4}$" o bien r"^[0-9]{2}[A-Z][a-z]{4}$"

Alianza para los objetivos: 17Aplo 🡪  r"^\d{2}[A-Z][a-z]{3}$" o bien r"^[0-9]{2}[A-Z][a-z]{3}$"
'''

import re

# Diccionario (codigo/texto)
ods_dict = {
    "1Fdlp": "Fin de la pobreza",
    "2Hc": "Hambre cero",
    "3Syb": "Salud y bienestar",
    "4Edc": "Educación de calidad",
    "5Idg": "Igualdad de género",
    "6Alys": "Agua limpia y saneamiento",
    "7Eaync": "Energía asequible y no contaminante",
    "8Tdyce": "Trabajo decente y creciente económico",
    "9Iiei": "Industria, innovación e infraestructura",
    "10Rdld": "Reducción de las desigualdades",
    "11Cycs": "Ciudades y comunidades sostenibles",
    "12Pycr": "Producción y consumo responsables",
    "13Apec": "Acción por el clima",
    "14Vs": "Vida submarina",
    "15Vdet": "Vida de ecosistemas terrestres",
    "16Pjeis": "Paz, justicia e instituciones sólidas",
    "17Aplo": "Alianza para los objetivos"
}

# Verificar formato
patron = r"^\d{1,2}[A-Z][a-z]{1,4}$"

# Mostrar lista/opciones
print("Listado de ODS:")
for codigo, nombre in ods_dict.items():
    print(f"{codigo}: {nombre}")
print("\nIntroduce un código (o 'FIN' para salir):")

# Pedimos codigo
while True:
    codigo = input().strip()  
    if codigo == "FIN":
        print("Programa terminado.")
        break
    if re.match(patron, codigo) and codigo in ods_dict:
        print(f"ODS válido: {ods_dict[codigo]}")
    else:
        print("Código no válido.")
    print("\nIntroduce otro código (o 'FIN' para salir):")

