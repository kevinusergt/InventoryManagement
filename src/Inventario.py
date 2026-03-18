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
  
  if len(inventario) == 0:
   print('El inventario está vacío!\n')
   time.sleep(0.5)
  else:
    for i in inventario: 
      print(f"Producto: {i['Nombre']} | Precio: {i['Precio']} $ | Cantidad: {i['Cantidad']} unidades \n")
    time.sleep(1)

def calcular_inventario():
  if len(inventario) == 0:
    print('inventario vacio')
  else:
    
    stock = len(inventario)
    
    
    calcular = sum(i['Precio'] * i['Cantidad'] for i in inventario)
    print('---REPORTE DE INVENTARIO---')
    print(f'Total de productos: {stock}')
    print(f'El valor total del inventario: {calcular} $')
      
    

def actualizar_inventrio():
  if len (inventario) == 0:
    print('El inventario está vacio!')        

def menu():
   
 print("||Menu Inventario|| \n")
 print("1. Registrar productos")
 print("2. Mostar inventario")
 print('3. Calcular estadisticas')
 print("4. Actualizar inventario")
 print("5. Eliminar producto")
 print("6. salir \n")





while True:
 menu()
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
  registrar_productos(nombre,precio,cantidad)     
  
 elif option == 2:
   mostrar_inventario()

 elif option == 3:
   calcular_inventario()
   print()
   time.sleep(1)

 elif option == 4:
   print('Aun en proceso \n') 
 
 elif option == 5:
   print('Aun en proceso \n') 
 
 
 elif option == 6:
   time.sleep(1)
   break
  
 else:
    print('Ingrese una opcion del menú \n')
    time.sleep(1)     
