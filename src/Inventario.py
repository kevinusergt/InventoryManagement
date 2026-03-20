import time


inventario = []

def registrar_productos(nombre, precio, cantidad):
  
  producto = {
   'Nombre': nombre,
   'Precio': precio,
   'Cantidad': cantidad
  }
  inventario.append(producto)
  print("Producto Agregado! \n")
  time.sleep(1)

def mostrar_inventario():
    for i in inventario: 
      print(f"Producto: {i['Nombre']} | Precio: {i['Precio']} $ | Cantidad: {i['Cantidad']} unidades \n")
    time.sleep(1)
 
def actualizar_producto(nombre, nuevo_nombre, nuevo_precio, nueva_cantidad):
    
    nombre['Nombre'] = nuevo_nombre
    nombre['Precio'] = nuevo_precio
    nombre['Cantidad'] = nueva_cantidad
    print("\n ¡Producto actualizado con éxito!")

def eliminar_producto(producto_eliminado):
  inventario.remove(producto_eliminado)
  
  
   
    
def calcular_inventario():
  if len(inventario) == 0:
    print('inventario vacio')
  else:
    
    stock = len(inventario)
    
    
    calcular = sum(i['Precio'] * i['Cantidad'] for i in inventario)
    print('---REPORTE DE INVENTARIO---')
    print(f'Total de productos: {stock}')
    print(f'El valor total del inventario: {calcular} $')
      
def menu():
   
 print("||Menu Inventario|| \n")
 print("1. Registrar productos")
 print("2. Mostar inventario")
 print('3. Calcular estadisticas')
 print("4. Actualizar inventario")
 print("5. Eliminar producto")
 print("6. salir \n")




