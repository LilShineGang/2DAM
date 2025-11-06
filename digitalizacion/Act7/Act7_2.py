import re

# Texto con los datos
texto = """
Juan Garcia - +34 900123456 - Alicante
Maria Lopez - 912345678 - Madrid
Juan Garcia - +34 900654321 - Alicante
Carlos Torres - +33 145678901 - Paris
Ana Gomez - 955112233 - Sevilla
Juan Garcia - +34 900777888 - Alicante
Pablo Diaz - 980223344 - Leon
Laura Sanchez - +34 900111999 - Alicante
Jorge Ramirez - 932221111 - Barcelona
Juan Garcia - +34 600333444 - Valencia
Sofia Perez - +44 207123456 - Londres
Pedro Alvarez - 900222333 - Murcia
Juan Garcia - +34 900999000 - Alicante
Raul Fernandez - 955678901 - Sevilla
Isabel Roca - +34 911456789 - Madrid
Juan Garcia - 900888777 - Alicante
Clara Morales - +34 900444555 - Alicante
Miguel Torres - 922456789 - Tenerife
Paula Vazquez - +34 900222333 - Alicante
Hugo Lopez - 934556677 - Barcelona
Carmen Flores - +34 900666777 – Alicante
"""

patron = r"(Juan Garcia)\s*-\s*(\+34\s?\d+)\s*-\s*Alicante"
coincide = re.findall(patron, texto)

print("Telefonos de Juan Garcia en Alicante que empiezan por +34:")
for nombre, telefono in coincide:
    print(f"{nombre} - {telefono}")
