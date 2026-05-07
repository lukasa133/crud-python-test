#TEST INVENTARIO
from source.inventario import Inventario

#TEST DE AGREGAR PRODUCTO, DEBE CONFIRMAR SI SE ESTA AGREGANDO
def test_agregar_producto():
    inventario = Inventario()


    inventario.agregar_producto("Mouse", 10)


    assert len(inventario.productos) == 1

#TEST ACTUALIZAR PRODUCTO, DEBE VALIDAR SI SE CAMBIO EL VALOR DE ALGUNOS DE LOS ATRIBUTOS
def test_actualizar_producto():
    inventario = Inventario()

    inventario.agregar_producto("Mouse", 5)

    inventario.actualizar_producto("Mouse", 10)

    producto = inventario.consultar_producto("Mouse")


    assert producto ["cantidad"] == 10

#TEST CONSULTAR PRODUCTO SI ESTA DENTRO DE LA LISTA
def test_consultar_producto():
    inventario = Inventario()

    inventario.agregar_producto("Pan", 14)

    producto = inventario.consultar_producto("Pan")

    assert producto["nombre"] == "Pan"

    assert producto["cantidad"] == 14


# ELIMINAR PRODUCTO Y VERIFICAR QUE ESTA FUNCIONANDO EL METODO DE ELIMINAR
def test_eliminar_producto():
    inventario = Inventario()

    inventario.agregar_producto("Banana", 8)

    inventario.eliminar_producto("Banana")

    assert len(inventario.productos) == 0

# CONFIRMAR SI SE ESTA LISTANDO LOS PRODUCTOS
def test_listar_productos():
    inventario = Inventario()

    inventario.agregar_producto("Mouse", 10)
    inventario.agregar_producto("Teclado", 5)

    productos = inventario.listar_productos()

    assert len(productos) == 2
    assert productos[0]["nombre"] == "Mouse"
    assert productos[1]["nombre"] == "Teclado"




