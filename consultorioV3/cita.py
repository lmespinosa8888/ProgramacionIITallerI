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


def calcular_ingresos(citas):
    return sum(cita.calcular_total() for cita in citas)


def contar_atenciones(citas, tipo_atencion):
    return sum(
        cita.usuario.tipo_atencion == tipo_atencion
        for cita in citas
    )