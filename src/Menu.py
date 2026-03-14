
import time


inventario = []

def menu():
   
 print("||Menu Inventario|| \n")
 print("1. Registrar productos")
 print("2. Mostar inventario")
 print("3. Calcular estadisticas")
 print("4. salir \n")





while True:
 menu()
 try:
  option = int(input("Choose an opcion: \n"))

 except ValueError:
  print("Enter a valid opcion!")
  time.sleep(1)
  continue
 

 if option == 1:
  nombre = input("Introduce el nombre del producto: ")
  while True:
    try:
      precio = float(input("Ingrese el precio: "))
      break
    except ValueError:
      print('Por favor ingresa un precio con decimales!')

  while True:  
    try:
      cantidad = int(input("Ingrese la cantidad: "))
      break  
    except ValueError:
     print('Ingresa un numero entero!')  
      
  

  producto = {
   'Nombre': nombre,
   'Precio': precio,
   'Cantidad': cantidad
  }
  inventario.append(producto)
  print("Producto Agregado \n")
  time.sleep(1)

 elif option == 2:
  if len(inventario) == 0:
   print('El inventario está vacío!')
   time.sleep(0.5)
  else:
    for i in inventario: 
      print(f"Nombre: {i['Nombre']} | Precio: {i['Precio']} $ | Cantidad: {i['Cantidad']} \n")
    time.sleep(1)


 elif option == 3:
  print("Despues")
     
 elif option == 4:
  print("Chao")
  time.sleep(1) 
  break
 
