VALOR_CITA = {
    "Particular": 80000,
    "EPS": 5000,
    "Prepagada": 30000
}

TIPOS_CLIENTE = ("Particular", "EPS", "Prepagada")
TIPOS_ATENCION = ("Limpieza", "Calzas", "Extracción", "Diagnóstico")
PRIORIDADES = ("Normal", "Urgente")


VALOR_ATENCION = {
    "Particular": {
        "Limpieza": 60000,
        "Calzas": 80000,
        "Extracción": 100000,
        "Diagnóstico": 50000
    },

    "EPS": {
        "Limpieza": 0,
        "Calzas": 40000,
        "Extracción": 40000,
        "Diagnóstico": 0
    },

    "Prepagada": {
        "Limpieza": 0,
        "Calzas": 10000,
        "Extracción": 10000,
        "Diagnóstico": 0
    }
}


def calcular_valor(tipo_cliente, tipo_atencion, cantidad):
    valor_cita = VALOR_CITA[tipo_cliente]

    valor_atencion = VALOR_ATENCION[tipo_cliente][tipo_atencion]

    total = valor_cita + (valor_atencion * cantidad)

    return total


def obtener_tipo_cliente(opcion):
    return TIPOS_CLIENTE[opcion - 1]


def obtener_tipo_atencion(opcion):
    return TIPOS_ATENCION[opcion - 1]


def obtener_prioridad(opcion):
    return PRIORIDADES[opcion - 1]


def requiere_cantidad(tipo_atencion):
    return tipo_atencion not in ("Limpieza", "Diagnóstico")