# Crear un diccionario con los apartados a), b) y c)
practicas = {
    "Transporte Sostenible": "Una empresa de transporte invierte en vehículos eléctricos o híbridos para reducir las emisiones de gases de efecto invernadero.",
    "Transparencia y Sostenibilidad": "Una empresa publica un informe anual de sostenibilidad que detalla sus acciones y logros en materia ambiental y social.",
    "Producción Limpia": "Una industria química actualiza sus equipos para utilizar procesos de producción más limpios y eficientes, minimizando la generación de residuos peligrosos."
}

# Agregar un nuevo par clave – valor relacionado con el apartado d)
practicas["Responsabilidad Laboral"] = "Una fábrica implementa programas de capacitación y seguridad laboral, así como políticas de equidad salarial y no discriminación."

# Agregar un nuevo par clave – valor relacionado con el apartado e)
practicas["Gestión del Agua"] = "Una planta de tratamiento de aguas residuales instala sistemas de filtración avanzados para eliminar contaminantes y reutilizar el agua en sus procesos."

# Mostrar el diccionario
for clave, valor in practicas.items():
    print(f"{clave}: {valor}")
