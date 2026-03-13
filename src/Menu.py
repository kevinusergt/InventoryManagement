
import time
def menu():
   
 print("||Menu Inventario|| \n")
 print("1. Registrar productos")
 print("2. Mostar inventario")
 print("3. Calcular estadisticas")
 print("4. salir \n")


option = 0
inventario = []


while option != 4:
 menu()
 try:
  option = int(input("Choose a opcion: \n"))

 except ValueError:
  print("Enter a valid opcion!")


 if option == 1:
  nombre = input("Introduce el nombre del producto: ")
  precio = float(input("Ingrese el precio: "))
  cantidad = int(input("Ingrese la cantidad: "))
  print("Producto Agregado \n")
  time.sleep(1)

  producto = {
   'Nombre': nombre,
   'Precio': precio,
   'Cantidad': cantidad
  }
  inventario.append(producto)

 elif option == 2:
  print(f"inventario: {inventario} \n")
  time.sleep(1)


 elif option == 4:
  print("SEE YOU!")
  break   
 
 elif option > 4:
  print("Introduzca una opcion del menu \n")
  time.sleep(1)