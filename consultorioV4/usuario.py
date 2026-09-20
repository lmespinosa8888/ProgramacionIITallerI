from datetime import datetime

class Usuario:
    MAX_CITAS_POR_FECHA = 8
    MAX_DIGITOS_IDENTIFICACION = 12
    MAX_DIGITOS_CARACTERES = 50
    MAX_CANTIDAD = 2
    citas_por_fecha = {}

    def __init__(
        self,
        cedula,
        nombre,
        telefono,
        tipo_cliente,
        tipo_atencion,
        cantidad,
        prioridad,
        fecha_cita
    ):
        # 1. Validación de Cédula
        if cedula is None or str(cedula).strip() == "":
            raise ValueError("La cédula no puede estar vacía.")
        if not str(cedula).isdigit():
            raise ValueError("La cédula debe contener solo números.")
        self.cedula = str(cedula).strip()
        if len(self.cedula) > self.MAX_DIGITOS_IDENTIFICACION:
            raise ValueError("La cédula no puede tener más de 12 números.")

        # 2. Validación de Nombre
        if nombre is None or str(nombre).strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.nombre = str(nombre).strip()
        if len(self.nombre) > self.MAX_DIGITOS_CARACTERES:
            raise ValueError("El nombre no puede tener más de 50 caracteres.")

        # 3. Validación de Teléfono
        if telefono is None or str(telefono).strip() == "":
            raise ValueError("El teléfono no puede estar vacío.")
        if not str(telefono).isdigit():
            raise ValueError("El teléfono debe contener solo dígitos.")
        self.telefono = str(telefono).strip()
        if len(self.telefono) > self.MAX_DIGITOS_IDENTIFICACION:
            raise ValueError("El teléfono no puede tener más de 12 números.")

        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion

        # 4. Validación de Cantidad
        if cantidad is None or str(cantidad).strip() == "":
            raise ValueError("La cantidad no puede estar vacía.")
        try:
            cantidad_int = int(cantidad)
            if cantidad_int <= 0:
                raise ValueError("La cantidad debe ser un número entero positivo mayor a cero.")
            if cantidad_int > self.MAX_CANTIDAD:
                raise ValueError("La cantidad máxima permitida es 2.")
            self.cantidad = cantidad_int
        except ValueError as e:
            if "invalid literal" in str(e):
                raise ValueError("La cantidad debe ser un número entero válido.")
            raise e

        self.prioridad = prioridad

        ## 5. Validación de Fecha de cita y límite de registros
        if fecha_cita is None or str(fecha_cita).strip() == "":
            raise ValueError("La fecha de cita no puede estar vacía.")
        
        # Validar formato de fecha
        try:
            if isinstance(fecha_cita, str):
                fecha_dt = datetime.strptime(fecha_cita.strip(), "%d-%m-%Y").date()
            else:
                fecha_dt = fecha_cita
        except ValueError:
            raise ValueError("La fecha de cita debe tener un formato válido (DD-MM-AAAA).")

        # Convertimos a string para usar como clave en el diccionario
        fecha_str = fecha_dt.strftime("%d-%m-%Y")

        # Verificar si la fecha ya alcanzó el cupo máximo (4 veces)
        conteo_actual = Usuario.citas_por_fecha.get(fecha_str, 0)
        if conteo_actual >= Usuario.MAX_CITAS_POR_FECHA:
            raise ValueError(f"La fecha {fecha_str} ya alcanzó el límite máximo de {Usuario.MAX_CITAS_POR_FECHA} citas.")

        # Si pasa todas las validaciones, asignamos la fecha e incrementamos el contador
        self.fecha_cita = fecha_dt
        Usuario.citas_por_fecha[fecha_str] = conteo_actual + 1
        
    def mostrar_datos(self):
        print(f"Cédula: {self.cedula}")
        print(f"Nombre: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Tipo de cliente: {self.tipo_cliente}")
        print(f"Tipo de atención: {self.tipo_atencion}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Prioridad: {self.prioridad}")
        print(f"Fecha de cita: {self.fecha_cita}")