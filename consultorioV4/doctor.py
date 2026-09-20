from collections import deque

# Agenda limitada para controlar las citas del doctor.
class Doctor:
    MAX_CITAS = 3

    def __init__(self, nombre, max_citas=MAX_CITAS):
        self.nombre = nombre
        self.citas = deque(maxlen=max_citas)

    def agregar_cita(self, cita):
        if len(self.citas) >= self.citas.maxlen:
            return False
        self.citas.append(cita)
        return True

    def tiene_cupo(self, citas_pendientes=0):
        return len(self.citas) + citas_pendientes < self.citas.maxlen

    def mostrar_doctor(self):
        print(f"Doctor: {self.nombre}")


# Colección de doctores disponibles para seleccionar.
doctores = deque([
    Doctor("Elon Musk"),
    Doctor("Jensen Huang"),
    Doctor("Satya Nadella"),
    Doctor("Sam Altman")
])


def mostrar_doctores():
    for indice, doctor in enumerate(doctores, start=1):
        print(f"{indice}. {doctor.nombre}")


def obtener_doctor(opcion):
    return doctores[opcion - 1]