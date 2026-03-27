import time  # Permite usar pausas con sleep
import src.servicios  # Importa funciones del módulo servicios
import src.archivos   # Importa funciones para manejar CSV


inventario = []  # Lista principal donde se almacenan los productos


# Bucle principal del programa (menú infinito)
while True:    
 src.servicios.menu()
 
 # Validación de entrada del usuario
 while True:
  try:
    option = int(input("Choose an opcion: \n"))
    break

  except ValueError:
    print("Enter a valid opcion! \n")
    time.sleep(1)
 

 # Opción 1: Registrar producto
 if option == 1:
  nombre = input("Introduce el nombre del producto: \n")
  
  # Validación de precio
  while True:
    try:
      precio = float(input("Ingrese el precio: \n"))
      if precio < 0:
        print('Ingrese un precio real!')
        continue
      break
    except ValueError:
      print('Por favor ingresa un precio con decimales!')

  # Validación de cantidad
  while True:  
    try:
      cantidad = int(input("Ingrese la cantidad: \n"))
      if cantidad < 0:
        print('Introduzca un numero entero positivo!')
        continue
      break  
    except ValueError:
     print('Ingresa un numero entero!')  
  
  # Guarda el producto
  src.servicios.registrar_productos(inventario,nombre,precio,cantidad)     
  

 # Opción 2: Mostrar inventario
 elif option == 2:
   if len(inventario) == 0:
    print('El inventario está vacío!\n')
    time.sleep(0.5)
    
   else: 
    src.servicios.mostrar_inventario(inventario)
    
    # Espera para volver al menú
    Volver = 0
    while Volver == 0:
      try:
       volver = int(input('Escriba un numero del 1-9 para volver al menu \n'))
       
       if 0 < volver < 10:
         print('Volviendo al menu... \n')
         time.sleep(1)
         break
       
       elif volver > 9:
         print('Ingrese un numero del rango.. \n')
       
       elif volver < 0:
         print('Ingrese un valor positivo \n')
         
      except ValueError:
       print('Ingrese un numero valido \n')


 # Opción 3: Estadísticas
 elif option == 3:
   if len(inventario) == 0:
     print('inventario vacio')
   else:  
     print(src.servicios.calcular_inventario(inventario))
    

 # Opción 4: Buscar producto
 elif option == 4:
   if len(inventario) ==0:
     print('El inventario está vacío')
   else:
     Buscar_product = input('Cual es el producto que desea buscar: ')
     print(src.servicios.buscar_producto(inventario,Buscar_product)) 


 # Opción 5: Actualizar producto
 elif option == 5:
   
   if len(inventario) == 0:
    print('Inventario vacio \n')
   else:
     nombre_buscar = input("Nombre del producto a buscar: ")

     # Busca el producto
     for producto in inventario:
        if producto['Nombre'].lower() == nombre_buscar.lower():
          
          print(f"Producto encontrado: {producto['Nombre']}")
          
          # Nuevo nombre
          n_nombre = input("Nuevo nombre: ")
          
          # Validación de precio
          while True:
            try:
              n_precio = float(input("Nuevo precio: "))
              if n_precio < 0:
                print('Ingrese un valor positivo')
                continue
              break
            except ValueError:
              print('Ingrese un precio valido')    
           
          # Validación de cantidad
          while True:
            try:    
              n_cantidad = int(input("Nueva cantidad: "))
              if n_cantidad < 0:
                print('Ingrese una cantidad valida')
                continue
              break
            except ValueError:
              print('Ingrese un numero entero')
          
          # Actualiza el producto
          src.servicios.actualizar_producto(producto, n_nombre, n_precio, n_cantidad)
          break
     
     # Si no lo encuentra
     else:
       print(f" Error: El producto '{nombre_buscar}' no existe. \n")
 

 # Opción 6: Eliminar producto
 elif option == 6:
   if len(inventario) == 0:
    print('Inventario vacio \n')
   else:
     nombre_eliminar = input("Nombre del producto a buscar: ")
     
     for producto in inventario:
        if producto['Nombre'].lower() == nombre_eliminar.lower():
          print(f"Producto {producto['Nombre']} encontrado")
          
          # Elimina el producto
          src.servicios.eliminar_producto(inventario, producto)
          print(f"Producto eliminado!")
          break
     else:# Mensaje si no existe
          print(f'El producto {nombre_eliminar} no existe!')


 # Opción 7: Guardar CSV
 elif option ==  7:
   if not inventario:
        print('Inventario Vacio')
   else:    
      Archivo = input('Ingrese el nombre de su archivo. ej (Datos.csv): ')
      src.archivos.guardar_CSV(inventario,Archivo)
      

 # Opción 8: Cargar CSV
 elif option == 8:
   Ruta = input('Ingrese el nombre o ruta del archivo. (ej: data.csv): ')
   inventario = src.archivos.cargar_CSV(Ruta,inventario)
                

 # Opción 9: Salir
 elif option == 9:
    print('Hasta luego, vuelve pronto')
    time.sleep(1)
    break
  

 # Opción inválida
 else:
    print('Ingrese una opcion del menú \n')
    time.sleep(1)     
