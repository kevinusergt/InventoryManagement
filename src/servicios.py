

# Registra un nuevo producto en el inventario
def registrar_productos(inventario,nombre,precio,cantidad): 
  producto = {
    "Nombre": nombre,
    "Precio": precio,
    "Cantidad": cantidad
  }   
  inventario.append(producto)  # Agrega el producto a la lista
  print("Producto Agregado! \n")
  

# Muestra todos los productos del inventario
def mostrar_inventario(inventario):
    for i in inventario: 
      print(f"Producto: {i['Nombre']} | Precio: {i['Precio']} $ | Cantidad: {i['Cantidad']} unidades \n")
    

# Actualiza los datos de un producto existente
def actualizar_producto(inventario, nuevo_nombre, nuevo_precio=0, nueva_cantidad=0):
    
    inventario['Nombre'] = nuevo_nombre
    inventario['Precio'] = nuevo_precio
    inventario['Cantidad'] = nueva_cantidad
    print("\n¡Producto actualizado con éxito!")


# Elimina un producto del inventario
def eliminar_producto(inventario, producto_eliminado):
  inventario.remove(producto_eliminado)
  

# Busca un producto por nombre (sin importar mayúsculas/minúsculas)
def buscar_producto(inventario,nombre):
  for producto in inventario:
    if producto['Nombre'].lower() == nombre.lower():
      return producto
  print(f'El producto {nombre} no fué encontrado')
  return None  
   
    
# Calcula estadísticas del inventario
def calcular_inventario(inventario):
  
    stock = len(inventario)  # Cantidad de productos distintos
    
    # Valor total del inventario (precio * cantidad)
    calcular = sum(i['Precio'] * i['Cantidad'] for i in inventario)
    
    # Producto más caro
    producto_mas_caro = max(inventario, key=lambda x: x['Precio'])
    
    # Producto con mayor cantidad
    Producto_de_mayor_stock = max(inventario, key=lambda x: x['Cantidad'])
    
    # Diccionario con resultados
    dictionary = {
      
        'Stock': stock,
        'Total inventario': calcular,
        'Producto mas caro': producto_mas_caro['Nombre'],
        'Producto mayor stock': Producto_de_mayor_stock['Nombre'] 
         }
    return dictionary
      

# Muestra el menú principal del sistema
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