# InventoryManagement

## Descripción
Este programa en Python que le permite al usuario interactuar através de un menú.
Dicho menú hace parte de un sistema de inventario para gestionar sus productos.


## Logica simple

* Se muestra el menú.
* Se recibe la opcion del usuario.
* Se llama a la respectiva funcion.

## Funcionalidades Principales

1. Agregar Producto.
2. Mostrar inventario.
3. Calcular estadisticas.
4. Buscar producto.
5. Eliminar producto.
6. Actualizar producto.
7. Guardar CSV.
8. Cargar CSV.
9. Salir

## Funciones
* `Menu()` -> Muestra las opciones disponibles.
* `Agregar_producto()` -> Agrega un nuevo producto al inventario.
* `Mostrar_inventario()` -> Muestra los productos del inventario.
* `Buscar_producto()` -> Busca y retorna el producto deseado.
* `Actualizar_producto()` -> Reemplaza un producto existente.
* `Eliminar_producto()`-> Elimina un producto dentro del inventario.
* `Calcular_estadisticas()` -> Retorna el valor total de los productos en el inventario.

## Ejemplo de uso
``` 
||Menu Inventario|| 

1. Registrar productos
2. Mostar inventario
3. Calcular estadisticas
4. Buscar producto
5. Actualizar inventario
6. Eliminar producto
7. Guardar CSV
8. Cargar CSV
9. salir 

Choose an opcion: 
1
Introduce el nombre del producto: 
pera
Ingrese el precio: 
1200
Ingrese la cantidad: 
3
Producto Agregado!
```

## Requisitos
* Ejecutar en consola o terminal.
* Python 3x
