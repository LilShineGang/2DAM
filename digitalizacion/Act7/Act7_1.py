import re

texto = """
Mi número de teléfono es 555-123-4567 y el de mi oficina es 555-987-6543.
Puedes escribirme al correo juan.perez@example.com o al alternativo jperez2025@mail.org.
También puedes visitar mi web en https://juanperez.dev/contacto.
"""

# 1. Números de teléfono
telefonos = re.findall(r"\d{3}-\d{3}-\d{4}", texto)  # \d significa cualquier dígito

# 2. Correos electrónicos
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", texto)
# [...] define un conjunto de caracteres permitidos
# \w significa cualquier carácter (letra mayúscula, minúscula, dígito o guión bajo _)

# 3. URLs
urls = re.findall(r"https?://[^\s]+", texto)
# ^ (dentro del corchete) niega el conjunto, es decir, “todo menos lo que sigue”
# ? significa que el carácter anterior puede aparecer 0 o 1 vez
# \s significa espacio, tabulación o salto de línea

print("Teléfonos:", telefonos)
print("Emails:", emails)
print("URLs:", urls)
