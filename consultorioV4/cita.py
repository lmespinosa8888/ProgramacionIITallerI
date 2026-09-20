from collections import deque

from servicios import calcular_valor


class Cita:
    def __init__(self, usuario, doctor):
        self.usuario = usuario
        self.doctor = doctor

    def calcular_total(self):
        return calcular_valor(
            self.usuario.tipo_cliente,
            self.usuario.tipo_atencion,
            self.usuario.cantidad
        )

    def mostrar_cita(self):
        print("\n----- DATOS DE LA CITA -----")
        print(f"Cliente: {self.usuario.nombre}")
        print(f"Doctor: {self.doctor.nombre}")
        print(f"Tipo de atención: {self.usuario.tipo_atencion}")
        print(f"Cantidad: {self.usuario.cantidad}")
        print(f"Prioridad: {self.usuario.prioridad}")
        print(f"Fecha: {self.usuario.fecha_cita}")
        print(f"Valor a pagar: ${self.calcular_total():,}")


def mostrar_citas(citas):
    for cita in citas:
        cita.mostrar_cita()

# Cola con las citas aceptadas después del procesamiento.
def procesar_citas(cola_atencion):

    citas_atendidas = deque()
    while cola_atencion:
        cita = cola_atencion.popleft()
        if cita.doctor.agregar_cita(cita):
            citas_atendidas.append(cita)
        else:
            print(
                f"La agenda de {cita.doctor.nombre} está llena. "
                f"La cita de {cita.usuario.nombre} no fue registrada."
            )
    return citas_atendidas


def calcular_ingresos(citas):
    return sum(cita.calcular_total() for cita in citas)


def contar_atenciones(citas, tipo_atencion):
    return sum(
        cita.usuario.tipo_atencion == tipo_atencion
        for cita in citas
    )