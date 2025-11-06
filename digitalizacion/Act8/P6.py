# Programa 6: Ciberseguridad - Informe de actividad sospechosa

# Se importa la clase canvas del paquete reportlab.pdfgen
# reportlab es una librería externa para generar PDFs en Python.
# canvas es la API de bajo nivel para dibujar texto, líneas e imágenes en páginas PDF.
from reportlab.pdfgen import canvas

pdf = canvas.Canvas("Informe_seguridad.pdf")
pdf.drawString(100, 800, "Reporte de Seguridad - Sistema Central")
pdf.drawString(100, 770, "Fecha: 01/10/2025")
pdf.drawString(100, 740, "Actividad sospechosa detectada en el servidor #12")
pdf.drawString(100, 710, "Acciones recomendadas: revisar logs y cambiar contraseñas.")
pdf.save()

print("Informe PDF generado correctamente.")
