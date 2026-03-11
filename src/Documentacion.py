# Solicitar el nombre del producto al usuario
Nombre = input("Enter the name: ")

# Inicializar la variable precio
precio = 0.0

# Bucle para solicitar el precio hasta que el usuario ingrese un número válido
while True:
    try:
        precio = float(input("Enter the price: "))
        break
    except ValueError:
        print("Enter a correct value: ")

# Inicializar la variable cantidad
cantidad = 0

# Bucle para solicitar la cantidad hasta que el usuario ingrese un número entero válido
while True:
    try:
        cantidad = int(input("Enter a quantity: "))
        break
    except ValueError:
        print("Error, Enter a correct value: ")

# Calcular el costo total multiplicando el precio por la cantidad
costo_total = precio * cantidad

# Mostrar la información del producto y el costo total formateado
print(f"Producto: {Nombre} | precio: {precio:.3f} $| cantidad: {cantidad} | costo total: {costo_total:.3f} $")

# El programa solicita el Nombre, el precio y la cantidad del o los productos
# Luego multiplica la cantidad de producto(s) por el valor unitario
# Para finalmente imprimir el nombre, el precio unitario, la cantidad y el costo total del inventario