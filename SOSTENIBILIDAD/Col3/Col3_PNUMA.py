
def main():

    respuestas = {
        'A': '1972',
        'B': ('Supervisar el estado del medio ambiente, aportar datos científicos a los gobiernos '
              'y coordinar respuestas a los desafíos globales.'),
        'C': ('Contaminación del aire', 'Gestión del agua', 'Conservación de ecosistemas', 'Educación ambiental'),
        'D': ['Prohibición de sustancias nocivas', 'Promoción de energías limpias', 'Control de residuos', 'Impulso de la economía circular'],
        'E': ['Protección mediante áreas protegidas', 'Defensa de especies en peligro', 'Integración de la sostenibilidad en políticas nacionales'],
        'F': 'El Protocolo de Kioto (1997) fijó compromisos internacionales de reducción de emisiones.',
        'G': 'Los Acuerdos de París (2015).',
        'H': 'Limitar el calentamiento global.'
    }

    opcion = input('Introduce un apartado (a-h): ').strip()
    if not opcion:
        print('No se ha introducido ninguna opción.')
        print('Hasta pronto')
        return

    letra = opcion[0].upper()

    if letra not in respuestas:
        print(f'Opción no esperada: "{opcion}". Introduce una letra entre a y h.')
        print('Hasta pronto')
        return

    respuesta = respuestas[letra]

    print('\n--- Respuesta ---')
    if isinstance(respuesta, (list, tuple)):
        for i, item in enumerate(respuesta, start=1):
            print(f'{i}. {item}')
    else:
        print(respuesta)
    print('--- Fin ---\n')

    print('Hasta pronto')


if __name__ == '__main__':
    main()
