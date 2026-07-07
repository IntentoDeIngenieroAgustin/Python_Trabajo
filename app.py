LIMITE_EXTRACCION = 20000


def cargar_usuarios():

    usuarios = {}

    archivo = open("usuarios.txt", "r")

    for linea in archivo:

        datos = linea.strip().split(",")

        usuario = datos[0]
        contraseña = datos[1]
        saldo = float(datos[2])

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


def registrar_operacion(usuario, operacion):

    archivo = open("historial.txt", "a")

    archivo.write(usuario + " - " + operacion + "\n")

    archivo.close()


def consultar_saldo(usuario, usuarios):

    saldo = usuarios[usuario]["saldo"]

    print("\n===== CONSULTA DE SALDO =====")
    print("Su saldo actual es: $", saldo)
    registrar_operacion(usuario, "Consultó su saldo. Saldo: $" + str(saldo))


def guardar_usuarios(usuarios):

    archivo = open("usuarios.txt", "w")

    for usuario in usuarios:

        contraseña = usuarios[usuario]["contraseña"]
        saldo = usuarios[usuario]["saldo"]

        archivo.write(usuario + "," + contraseña + "," + str(saldo) + "\n")

    archivo.close()


def depositar(usuario, usuarios):

    print("\n===== DEPÓSITO =====")

    monto = int(input("Ingrese el monto a depositar: $"))

    if monto > 0:

        usuarios[usuario]["saldo"] += monto

        guardar_usuarios(usuarios)

        registrar_operacion(usuario, "Depositó $" + str(monto))

        print("Depósito realizado con éxito.")
        print("Nuevo saldo: $", usuarios[usuario]["saldo"])

    else:

        print("El monto debe ser mayor que cero.")


def extraer(usuario, usuarios):

    print("\n===== EXTRACCIÓN =====")

    while True:

        try:
            monto = int(
                input("Ingrese el monto a extraer ($0 para cancelar): "))
        except ValueError:
            print("Debe ingresar un número.")
            continue

        if monto == 0:
            print("Operación cancelada.")
            break

        elif monto < 0:
            print("El monto debe ser mayor que cero.")

        elif monto > LIMITE_EXTRACCION:
            print("No puede extraer más de $", LIMITE_EXTRACCION)

        elif monto > usuarios[usuario]["saldo"]:
            print("Saldo insuficiente.")

        else:

            usuarios[usuario]["saldo"] -= monto

            guardar_usuarios(usuarios)

            registrar_operacion(
                usuario,
                "Extrajo $" + str(monto) +
                ". Saldo actual: $" + str(usuarios[usuario]["saldo"])
            )

            print("\nExtracción realizada con éxito.")
            print("Saldo restante: $", usuarios[usuario]["saldo"])

            break


def transferir(usuario, usuarios):

    print("\n===== TRANSFERENCIA =====")

    destinatario = input("Ingrese el usuario destinatario: ")

    if destinatario not in usuarios:
        print("El usuario no existe.")
        return

    if destinatario == usuario:
        print("No puede transferirse dinero a usted mismo.")
        return

    while True:

        try:
            monto = int(
                input("Ingrese el monto a transferir ($0 para cancelar): "))
        except ValueError:
            print("Debe ingresar un número.")
            continue

        if monto == 0:
            print("Operación cancelada.")
            break

        elif monto < 0:
            print("El monto debe ser mayor que cero.")

        elif monto > usuarios[usuario]["saldo"]:
            print("Saldo insuficiente.")

        else:

            usuarios[usuario]["saldo"] -= monto
            usuarios[destinatario]["saldo"] += monto

            guardar_usuarios(usuarios)

            registrar_operacion(
                usuario,
                "Transfirió $" + str(monto) + " a " + destinatario +
                ". Saldo actual: $" + str(usuarios[usuario]["saldo"])
            )

            registrar_operacion(
                destinatario,
                "Recibió $" + str(monto) + " de " + usuario +
                ". Saldo actual: $" + str(usuarios[destinatario]["saldo"])
            )

            print("\nTransferencia realizada con éxito.")
            print("Su nuevo saldo es: $", usuarios[usuario]["saldo"])

            break


def ver_historial(usuario):

    print("\n===== HISTORIAL DE OPERACIONES =====")

    try:

        archivo = open("historial.txt", "r")

        encontrado = False

        for linea in archivo:

            if linea.startswith(usuario + " - "):
                print(linea.strip())
                encontrado = True

        archivo.close()

        if not encontrado:
            print("No hay operaciones registradas.")

    except FileNotFoundError:

        print("Todavía no existe el historial.")


def menu(usuario, usuarios):

    opcion = 0

    while opcion != 6:

        print("\n===== MENÚ PRINCIPAL =====")
        print("Bienvenido,", usuario)
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Extraer dinero")
        print("4. Transferir dinero")
        print("5. Ver historial")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            consultar_saldo(usuario, usuarios)

        elif opcion == 2:
            depositar(usuario, usuarios)

        elif opcion == 3:
            extraer(usuario, usuarios)

        elif opcion == 4:
            transferir(usuario, usuarios)

        elif opcion == 5:

            ver_historial(usuario)

        elif opcion == 6:

            print("Gracias por utilizar el cajero.")

        else:
            print("Opción inválida.")


def main():

    usuarios = cargar_usuarios()

    usuario_actual = login(usuarios)

    if usuario_actual != None:
        menu(usuario_actual, usuarios)


main()
