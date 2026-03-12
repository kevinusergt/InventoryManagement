def menu():
   
 print("||Menu Inventario|| \n")
 print("1. Registrar productos")
 print("2. Mostar inventario")
 print("3. Calcular estadisticas")
 print("4. salir")

opcion = 0

while opcion < 4:
 menu()
 try:
    opcion = int(input("Eliga una opcion: "))
    break

 except ValueError:
    print("Ingresa una opcion valida")

while opcion > 4:
  print("Ingresa una opcion del menu")
  menu()
  try:
    opcion = int(input("Eliga una opcion: "))
    break
  except ValueError:
     print("Ingresa una opcion valida")
   

   

if opcion == 1:
        
    nombre = input("Ingrese el nombre del producto: \n")
    precio = float(input("Ingrese el precio: \n"))
    cantidad = int(input("Ingrese la cantidad: \n"))

elif opcion== 2:

    print("Coming soon")    

