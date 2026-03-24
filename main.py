import time
import src.Inventario

inventario = []

while True:
 src.Inventario.menu()
 while True:
  try:
    option = int(input("Choose an opcion: \n"))
    break

  except ValueError:
    print("Enter a valid opcion! \n")
    time.sleep(1)
 

 if option == 1:
  nombre = input("Introduce el nombre del producto: \n")
  while True:
    try:
      precio = float(input("Ingrese el precio: \n"))
      if precio < 0:
        print('Ingrese un precio real!')
        continue
      break
    except ValueError:
      print('Por favor ingresa un precio con decimales!')

  while True:  
    try:
      cantidad = int(input("Ingrese la cantidad: \n"))
      if cantidad < 0:
        print('Introduzca un numero entero positivo!')
        continue
      break  
    except ValueError:
     print('Ingresa un numero entero!')  
  
  src.Inventario.registrar_productos(inventario, nombre, precio, cantidad)     
  
 elif option == 2:
   if len(inventario) == 0:
    print('El inventario está vacío!\n')
    time.sleep(0.5)
    
   else: 
    src.Inventario.mostrar_inventario(inventario)
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

 elif option == 3:
   if len(inventario) == 0:
    print('inventario vacio')
   else:  
    src.Inventario.calcular_inventario(inventario)
    print()
    time.sleep(1)

 elif option == 4:
   
   if len(inventario) == 0:
    print('Inventario vacio \n')
   else:
     nombre_buscar = input("Nombre del producto a buscar: ")

     for producto in inventario:
        if producto['Nombre'].lower() == nombre_buscar.lower():
          
          print(f"Producto encontrado: {producto['Nombre']}")
          
          n_nombre = input("Nuevo nombre: ")
          while True:
            try:
              n_precio = float(input("Nuevo precio: "))
              if n_precio < 0:
                print('Ingrese un valor positivo')
                continue
              break
            except ValueError:
              print('Ingrese un precio valido')    
           
          while True:
            try:    
              n_cantidad = int(input("Nueva cantidad: "))
              if n_cantidad < 0:
                print('Ingrese una cantidad valida')
                continue
              break
            except ValueError:
              print('Ingrese un numero entero')
          
          src.Inventario.actualizar_producto(producto, n_nombre, n_precio, n_cantidad)
          break
     else:
       print(f" Error: El producto '{nombre_buscar}' no existe. \n")
 
 elif option == 5:
   if len(inventario) == 0:
    print('Inventario vacio \n')
   else:
     nombre_eliminar = input("Nombre del producto a buscar: ")
     
     for producto in inventario:
        if producto['Nombre'].lower() == nombre_eliminar.lower():
          print(f"Producto {producto['Nombre']} encontrado")
          src.Inventario.eliminar_producto(producto)
          print(f"Producto eliminado!")
          break
    
       
        else:
          print(f'El producto {nombre_eliminar} no existe!') 
       
        
 elif option == 6:
    print('Hasta luego, vuelve pronto')
    time.sleep(1)
    break
  
 else:
    print('Ingrese una opcion del menú \n')
    time.sleep(1)     

