#TEST PRODUCTO
def test_agregar_producto():
    inventario = Inventario()


    inventario.agregar_producto("Mouse", 10)


    assert len(inventario.productos) == 1