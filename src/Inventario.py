import time


inventario = []

def registrar_productos(Nombre, Precio, Cantidad):
  
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

def actualizar_inventrio():
  if len (inventario) == 0:
    print('El inventario está vacio!')        

def menu():
   
 print("||Menu Inventario|| \n")
 print("1. Registrar productos")
 print("2. Mostar inventario")
 print("3. Actualizar inventario")
 print("4. Eliminar producto")
 print("5. salir \n")





while True:
 menu()
 try:
  option = int(input("Choose an opcion: \n"))

 except ValueError:
  print("Enter a valid opcion!")
  time.sleep(1)
 

 if option == 1:
  nombre = input("Introduce el nombre del producto:\n ")
  while True:
    try:
      precio = float(input("Ingrese el precio: \n "))
      break
    except ValueError:
      print('Por favor ingresa un precio con decimales!')

  while True:  
    try:
      cantidad = int(input("Ingrese la cantidad: \n"))
      break  
    except ValueError:
     print('Ingresa un numero entero!')  
  registrar_productos(nombre,precio,cantidad)     
  
 elif option == 2:
   mostrar_inventario()

 elif option == 3:
   print('Aun en proceso')

 elif option == 4:
   print('Aun en proceso') 

 elif option == 5:
   time.sleep(1)
   break
       
