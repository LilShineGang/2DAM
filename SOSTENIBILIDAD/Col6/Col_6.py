p_ods = {
    "Austria": 4,
    "Bélgica": 16,
    "Bulgaria": 31,
    "Chipre": 32,
    "Croacia": 14,
    "Dinamarca": 2,
    "Eslovaquia": 23,
    "Eslovenia": 8,
    "España": 20,
    "Estonia": 18,
    "Finlandia": 1,
    "Francia": 7,
    "Grecia": 28,
    "Hungría": 25,
    "Irlanda": 19,
    "Italia": 15,
    "Letonia": 21,
    "Lituania": 26,
    "Luxemburgo": 27,
    "Malta": 24,
    "Países Bajos": 17,
    "Polonia": 11,
    "Portugal": 22,
    "República Checa": 9,
    "Rumanía": 29,
    "Suecia": 3,
    "Alemania": 6
}

for pais, pos in p_ods.items():
    barra = "*" * pos
    print(pais, "  \t", barra)
