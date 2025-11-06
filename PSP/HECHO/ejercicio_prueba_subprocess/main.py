import subprocess

def main():
    print(
        "1.- Navegador web"
        + "\n" + "2.- Procesador de textos"
        + "\n " + "3.- Editor de textos"
        + "\n" + "4.- Calculadora"
        + "\n" + "5.- Ping a un host"
        + "\n" + "0.- Salir"
    )

    opcion = int(input("Seleccione una opcion: "))

    while opcion != 0:
        if opcion == 1:
            subprocess.run(["zen-browser"])
        elif opcion == 2:
            subprocess.run(["libreoffice", "--writer"])
        elif opcion == 3:
            subprocess.run(["nano"])
        elif opcion == 4:
            subprocess.run(["gnome-calculator"])
        elif opcion == 5:
            host = input("Ingrese el host a hacer ping: ")
            subprocess.run(["ping", "-c", "4", host])
        else:
            print("Opcion no valida.")

        print(
            "1.- Navegador web"
            + "\n" + "2.- Procesador de textos"
            + "\n " + "3.- Editor de textos"
            + "\n" + "4.- Calculadora"
            + "\n" + "5.- Ping a un host"
            + "\n" + "0.- Salir"
        )
        opcion = int(input("Seleccione una opcion: "))

if __name__ == "__main__":
    main()