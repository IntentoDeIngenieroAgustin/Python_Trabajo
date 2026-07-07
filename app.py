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


def main():

    usuarios = cargar_usuarios()

    usuario_actual = login(usuarios)

    if usuario_actual != None:
        print("Login exitoso.")
    else:
        print("No se pudo iniciar sesión.")


main()
