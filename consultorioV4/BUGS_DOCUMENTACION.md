## 🟢 Bugs Solucionados

### 1. Reintento automático ante datos incorrectos o fuera de rango
* **Descripción:** Si el usuario ingresaba un valor inválido (como letras en campos numéricos o números fuera de las opciones permitidas), el sistema fallaba o no daba opción de corrección.
* **Solución:** Se implementaron bucles de validación continua (`while True`) en las funciones de entrada de datos. Cuando se ingresa un valor erróneo, el programa muestra un mensaje de advertencia y solicita el dato nuevamente hasta que sea correcto[cite: 8].

### 2. Restricción en la cantidad permitida de atenciones
* **Descripción:** Se podían ingresar números enteros negativos, cero o cantidades excesivas en las atenciones que lo requerían.
* **Solución:** Se estableció la constante `MAX_CANTIDAD = 2` y se añadió una validación estricta para asegurar que la cantidad ingresada sea un entero positivo dentro del rango permitido (entre 1 y 2).

### 3. Limitar la cantidad de citas para un solo doctor
* **Descripción:** Los doctores no tenían un tope máximo de atenciones, permitiendo asignarles un número ilimitado de citas sin control de agenda.
* **Solución:** Se integró la estructura `collections.deque` con un límite máximo de elementos (`maxlen = MAX_CITAS`) dentro de la clase `Doctor`. Antes de registrar una cita, el sistema verifica que el médico aún tenga cupo disponible.

### 4. Control y validación de cantidad de caracteres
* **Descripción:** No existía un límite en la longitud de las entradas de texto, permitiendo cadenas vacías o textos excesivamente largos.
* **Solución:** Se crearon constantes globales (`MAX_DIGITOS_CARACTERES = 50` y `MAX_DIGITOS_IDENTIFICACION = 12`) y funciones de validación como `pedir_caracteres()` y `pedir_numero()` que verifican la longitud máxima de los campos.

---

## 🔴 Bugs Pendientes

### 1. Limitar la cantidad de citas de un mismo usuario
* **Estado:** Pendiente.
* **Descripción:** Un mismo cliente (identificado por su cédula) puede agendar múltiples citas sin ningún tipo de restricción o límite por día/sesión.
* **Impacto:** Un usuario puede monopolizar la agenda disponible.
* **Acción requerida:** Consultar el histórico o la cola de registros por número de cédula antes de autorizar la creación de una nueva cita.

### 2. Permitir agendar citas en fechas pasadas
* **Estado:** Pendiente.
* **Descripción:** La validación actual comprueba que la fecha cumpla con el formato `DD-MM-AAAA`, pero no verifica si la fecha ingresada es anterior al día actual.
* **Impacto:** Permite agendar citas en días o años que ya transcurrieron (ej. `01-01-2000`).
* **Acción requerida:** Comparar la fecha convertida contra la fecha actual (`datetime.now().date()`) y rechazar registros extemporáneos.

### 3. Nombres con caracteres numéricos o símbolos
* **Estado:** Pendiente.
* **Descripción:** El campo "Nombre" valida la cantidad máxima de caracteres y que no esté vacío, pero acepta entradas que contienen números o caracteres especiales (ej. `"Carlos123"` o `"Juan#$"`)[cite: 8].
* **Impacto:** Compromete la calidad e integridad de la información del cliente.
* **Acción requerida:** Implementar validaciones mediante expresiones regulares o métodos de cadena (como `.isalpha()`) para permitir únicamente letras y espacios.

```