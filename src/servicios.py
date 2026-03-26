

def registrar_productos(inventario,nombre,precio,cantidad): 
  producto = {
    "Nombre": nombre,
    "Precio": precio,
    "Cantidad": cantidad
  }   
  inventario.append(producto)
  print("Producto Agregado! \n")
  

def mostrar_inventario(inventario):
    for i in inventario: 
      print(f"Producto: {i['Nombre']} | Precio: {i['Precio']} $ | Cantidad: {i['Cantidad']} unidades \n")
    
 
def actualizar_producto(inventario, nuevo_nombre, nuevo_precio=0, nueva_cantidad=0):
    
    inventario['Nombre'] = nuevo_nombre
    inventario['Precio'] = nuevo_precio
    inventario['Cantidad'] = nueva_cantidad
    print("\n¡Producto actualizado con éxito!")

def eliminar_producto(inventario, producto_eliminado):
  inventario.remove(producto_eliminado)
  
def buscar_producto(inventario,nombre):
  for producto in inventario:
    if producto['Nombre'].lower() == nombre.lower():
      return producto
  print(f'El producto {nombre} no fué encontrado')
  return None  
   
    
def calcular_inventario(inventario):
  
    stock = len(inventario)
    calcular = sum(i['Precio'] * i['Cantidad'] for i in inventario)
    producto_mas_caro = max(inventario, key=lambda x: x['Precio'])
    Producto_de_mayor_stock = max(inventario, key=lambda x: x['Cantidad'])
    
    dictionary = {
      
        'Stock': stock,
        'Total inventario': calcular,
        'Producto mas caro': f'Nombre: {producto_mas_caro['Nombre']} || Precio: {producto_mas_caro['Precio']}$',
        'Producto mayor stock': f'Nombre: {Producto_de_mayor_stock['Nombre']} || Cantidad: {Producto_de_mayor_stock['Cantidad']} unidades'
         }
    return dictionary
      
def menu():
   
 print("||Menu Inventario|| \n")
 print("1. Registrar productos")
 print("2. Mostar inventario")
 print('3. Calcular estadisticas')
 print('4. Buscar producto')
 print("5. Actualizar inventario")
 print("6. Eliminar producto")
 print("7. Guardar CSV")
 print("8. Cargar CSV")
 print("9. salir \n")