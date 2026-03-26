import csv

def guardar_CSV(inventario,ruta,Incluir_Header=True):
    
    try:
        with open(ruta, 'w') as datos:
            Wr = csv.writer(datos)
            
            if Incluir_Header:
                Wr.writerow(['Nombre','Precio','Cantidad'])
            
            for producto in inventario:
                Wr.writerow([
                    producto['Nombre'],
                    producto['Precio'],
                    producto['Cantidad']
                ])    
        print(f'Inventario guardado en:{ruta}')
    except Exception as e:
        print(f'Error inesperado: {e}')        
                    





def cargar_CSV(ruta):
    pass