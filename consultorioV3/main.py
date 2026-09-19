from cita import Cita, calcular_ingresos, contar_atenciones, mostrar_citas
from doctor import doctores, mostrar_doctores, obtener_doctor
from servicios import (
    PRIORIDADES,
    TIPOS_ATENCION,
    TIPOS_CLIENTE,
    obtener_prioridad,
    obtener_tipo_atencion,
    obtener_tipo_cliente,
    requiere_cantidad,
)
from usuario import Usuario


def pedir_numero(mensaje, nombre, maximo_digitos):
    while True:
        valor = input(mensaje).strip()
        if not valor.isdigit():
            print(f"{nombre} debe contener solo números. Intente nuevamente.")
        elif len(valor) > maximo_digitos:
            print(f"{nombre} no puede tener más de {maximo_digitos} números.")
        else:
            return valor


def pedir_caracteres(mensaje, nombre, maximo_caracteres):
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print(f"{nombre} no puede estar vacío. Intente nuevamente.")
        elif len(valor) > maximo_caracteres:
            print(
                f"{nombre} no puede tener más de "
                f"{maximo_caracteres} caracteres. Intente nuevamente."
            )
        else:
            return valor


def pedir_opcion(mensaje, cantidad_opciones):
    while True:
        opcion = input(mensaje).strip()
        if opcion.isdigit() and 1 <= int(opcion) <= cantidad_opciones:
            return int(opcion)
        print("Opción inválida. Seleccione una opción de la lista e intente nuevamente.")


def mostrar_opciones(titulo, opciones):
    print(f"\n{titulo}:")
    for indice, opcion in enumerate(opciones, start=1):
        print(f"{indice}. {opcion}")


def pedir_cantidad():
    while True:
        valor = input(f"Cantidad (máximo {Usuario.MAX_CANTIDAD}): ").strip()
        try:
            cantidad = int(valor)
            if 1 <= cantidad <= Usuario.MAX_CANTIDAD:
                return cantidad
        except ValueError:
            pass
        print(
            "La cantidad debe ser un número entero entre 1 y "
            f"{Usuario.MAX_CANTIDAD}. Intente nuevamente."
        )


def pedir_tipo_cliente():
    mostrar_opciones("Tipo de cliente", TIPOS_CLIENTE)
    opcion = pedir_opcion("Seleccione una opción: ", len(TIPOS_CLIENTE))
    return obtener_tipo_cliente(opcion)


def pedir_tipo_atencion():
    mostrar_opciones("Tipo de atención", TIPOS_ATENCION)
    opcion = pedir_opcion("Seleccione una opción: ", len(TIPOS_ATENCION))
    return obtener_tipo_atencion(opcion)


def pedir_prioridad():
    mostrar_opciones("Prioridad", PRIORIDADES)
    opcion = pedir_opcion("Seleccione una opción: ", len(PRIORIDADES))
    return obtener_prioridad(opcion)


def pedir_doctor():
    print("\nDoctores disponibles:")
    mostrar_doctores()
    opcion = pedir_opcion("Seleccione un doctor: ", len(doctores))
    return obtener_doctor(opcion)


def crear_usuario(datos):
    while True:
        fecha_cita = input("Fecha de la cita (DD-MM-AAAA): ").strip()
        try:
            return Usuario(*datos, fecha_cita)
        except ValueError as error:
            print(f"{error} Intente nuevamente.")


def registrar_cita():
    print("\n========== REGISTRO DE CLIENTE ==========")
    cedula = pedir_numero(
        "Cédula: ", "La cédula", Usuario.MAX_DIGITOS_IDENTIFICACION
    )
    nombre = pedir_caracteres(
        "Nombre: ", "El nombre", Usuario.MAX_DIGITOS_CARACTERES
    )
    telefono = pedir_numero(
        "Teléfono: ", "El teléfono", Usuario.MAX_DIGITOS_IDENTIFICACION
    )
    tipo_cliente = pedir_tipo_cliente()
    tipo_atencion = pedir_tipo_atencion()
    cantidad = pedir_cantidad() if requiere_cantidad(tipo_atencion) else 1
    prioridad = pedir_prioridad()
    usuario = crear_usuario(
        (cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad)
    )
    return Cita(usuario, pedir_doctor())


def mostrar_resultados(clientes, citas):
    print("\n\n==========================================")
    print("       CLIENTES REGISTRADOS")
    print("==========================================")
    mostrar_citas(citas)

    print("\n\n==========================================")
    print("              RESULTADOS")
    print("==========================================")
    print(f"Total de clientes: {len(clientes)}")
    print(f"Ingresos totales: ${calcular_ingresos(citas):,}")
    print(f"Clientes con extracción: {contar_atenciones(citas, 'Extracción')}")

    print("\nCitas por fecha:")
    for fecha, cantidad in sorted(Usuario.citas_por_fecha.items()):
        print(f"{fecha}: {cantidad} cita(s)")

    print("\n\n==========================================")
    print("       CLIENTES ORDENADOS POR NOMBRE")
    print("==========================================")
    for cliente in sorted(clientes, key=lambda cliente: cliente.nombre):
        print(
            f"Cédula: {cliente.cedula} | "
            f"Nombre: {cliente.nombre} | "
            f"Tipo de cliente: {cliente.tipo_cliente} | "
            f"Atención: {cliente.tipo_atencion} | "
            f"Prioridad: {cliente.prioridad}"
        )


def ejecutar_programa():
    clientes = []
    citas = []
    continuar = "S"

    while continuar.upper() == "S":
        cita = registrar_cita()
        clientes.append(cita.usuario)
        citas.append(cita)
        print(f"\nCliente {cita.usuario.nombre} registrado correctamente.")
        continuar = input("\n¿Desea registrar otro cliente? (S/N): ")

    mostrar_resultados(clientes, citas)


if __name__ == "__main__":
    ejecutar_programa()
