Nombre= input("Enter the name: ")
precio= 0.0

while True:
    try:
        precio = float(input("Enter the price: "))
        break
    except ValueError:
        print("Enter a correct value: ")

cantidad= 0

while True:
    try:
        cantidad = int(input("Enter a quantity: "))
        break
    except ValueError:
        print("Error, Enter a correct value: ")