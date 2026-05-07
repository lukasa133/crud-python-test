from source.producto import Productos

def test_clase_producto():
    producto = Productos("Mouse", 10)

    assert producto.nombre == "Mouse"
    assert producto.cantidad == 10