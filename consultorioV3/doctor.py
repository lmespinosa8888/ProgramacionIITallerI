class Doctor:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_doctor(self):
        print(f"Doctor: {self.nombre}")


doctores = [
    Doctor("Elon Musk"),
    Doctor("Jensen Huang"),
    Doctor("Satya Nadella"),
    Doctor("Sam Altman")
]


def mostrar_doctores():
    for indice, doctor in enumerate(doctores, start=1):
        print(f"{indice}. {doctor.nombre}")


def obtener_doctor(opcion):
    return doctores[opcion - 1]