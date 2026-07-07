def cargar_usuarios():

    usuarios = {}

    archivo = open("usuarios.txt", "r")

    for linea in archivo:

        datos = linea.strip().split(",")

        usuario = datos[0]
        contraseña = datos[1]
        saldo = int(datos[2])

        usuarios[usuario] = {
            "contraseña": contraseña,
            "saldo": saldo
        }

    archivo.close()

    return usuarios


def login(usuarios):

    print("===== CAJERO AUTOMÁTICO =====")

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios:

        if usuarios[usuario]["contraseña"] == contraseña:

            print("\nBienvenido", usuario)

            return usuario

        else:

            print("\nContraseña incorrecta")

            return None

    else:

        print("\nUsuario inexistente")

        return None


def consultar_saldo(usuario, usuarios):

    saldo = usuarios[usuario]["saldo"]

    print("\n===== CONSULTA DE SALDO =====")
    print("Su saldo actual es: $", saldo)


def menu(usuario, usuarios):

    opcion = 0

    while opcion != 5:

        print("\n===== MENÚ PRINCIPAL =====")
        print("Bienvenido,", usuario)
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Extraer dinero")
        print("4. Transferir dinero")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            consultar_saldo(usuario, usuarios)

        elif opcion == 2:
            print("Depositar dinero")

        elif opcion == 3:
            print("Extraer dinero")

        elif opcion == 4:
            print("Transferir dinero")

        elif opcion == 5:
            print("Gracias por utilizar el cajero.")

        else:
            print("Opción inválida.")


def main():

    usuarios = cargar_usuarios()

    usuario_actual = login(usuarios)

    if usuario_actual != None:
        menu(usuario_actual, usuarios)


main()
