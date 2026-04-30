# Documentación del Proceso TDD – Sistema de Inventario

## 1. Análisis de Funcionalidades

Antes de iniciar el desarrollo del sistema, se identificaron las funcionalidades principales requeridas para el inventario.

### Funcionalidades del sistema

El sistema debe permitir:

* Registrar un producto en el inventario.
* Actualizar la cantidad disponible de un producto.
* Consultar la información de un producto.
* Listar todos los productos registrados.

### Verificación mediante pruebas

Cada funcionalidad será validada mediante pruebas automatizadas usando el enfoque TDD (Test-Driven Development).

Ejemplo:

* Si se registra un producto, debe almacenarse correctamente.
* Si se actualiza una cantidad, el valor debe cambiar.
* Si se consulta un producto, debe retornar la información correcta.
* Si se listan productos, debe devolver todos los registrados.

---

# 2. Configuración del Entorno

Para el desarrollo del proyecto se configuró el siguiente entorno:

### Herramientas utilizadas

* Lenguaje: Python
* Framework de pruebas: pytest
* Control de versiones: Git
* Repositorio remoto: GitHub
* IDE: Visual Studio Code

### Estructura del proyecto

```text
crud-python-test/
│
├── source/
│   ├── __init__.py
│   ├── inventario.py
│   └── producto.py
│
├── tests/
│   ├── __init__.py
│   ├── test_inventario.py
│   └── test_producto.py
│
├── README.md
└── requirements.txt
```

---

# 3. Aplicación del Ciclo TDD

## Funcionalidad 1: Agregar Producto

### RED – Prueba que falla

Se creó una prueba automatizada antes de implementar el método.

```python
def test_agregar_producto():
    inventario = Inventario()

    inventario.agregar_producto("Mouse", 10)

    assert len(inventario.productos) == 1
```

### Resultado esperado

La prueba debía fallar porque el método `agregar_producto()` aún no existía.

### Resultado obtenido

Se obtuvo un error indicando que el método no estaba definido.

```text
AttributeError: 'Inventario' object has no attribute 'agregar_producto'
```

Esto corresponde a la fase RED del TDD.

---

### GREEN – Código mínimo necesario

Se implementó el código mínimo para hacer pasar la prueba.

```python
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, cantidad):
        self.productos.append({
            "nombre": nombre,
            "cantidad": cantidad
        })
```

### Resultado

La prueba pasó correctamente.

---

### REFACTOR – Mejora del código

Después de hacer pasar la prueba, se realizaron mejoras en la estructura del código.

Ejemplos:

* Mejor organización de métodos.
* Separación entre lógica de inventario y modelo de producto.
* Mejora en nombres y estructura.

---

# 4. Repetición del Ciclo TDD

El ciclo TDD se repetirá para las siguientes funcionalidades:

* Actualizar cantidad.
* Consultar producto.
* Listar productos.

Cada funcionalidad seguirá el proceso:

1. Crear prueba que falle.
2. Implementar código mínimo.
3. Refactorizar.
4. Ejecutar nuevamente las pruebas.

---

# 5. Bitácora Reflexiva

## Reflexión del proceso

El uso de TDD permitió desarrollar funcionalidades de manera incremental y controlada.

La escritura de pruebas antes del código ayudó a:

* Detectar errores tempranamente.
* Validar cada funcionalidad.
* Mejorar la organización del código.
* Facilitar la refactorización.

Durante el proceso se identificó la importancia de:

* Mantener una estructura clara del proyecto.
* Comprender las importaciones en Python.
* Configurar correctamente pytest.
* Ejecutar pruebas desde la raíz del proyecto.

El enfoque TDD permitió trabajar de forma ordenada y asegurar que cada funcionalidad cumpliera con los requisitos establecidos.

---

# 6. Entregables

* Código fuente del sistema.
* Pruebas automatizadas.
* Repositorio Git.
* Bitácora reflexiva.
