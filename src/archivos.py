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
                    





def cargar_CSV(ruta, inventario_memoria):
    Productos_cargados =[]
    Filas_invalidas = 0
    
    try:
        with open(ruta,"r",newline='') as file:
            carga = csv.reader(file)
            
            encabezado = next(carga,None)
            if encabezado != ['Nombre','Precio','Cantidad']:
                print('Error, encabezado invalido. Debe ser: Nombre, Precio, Cantidad')
                return inventario_memoria
            
            for fila in carga:
                if len(fila) != 3:
                    Filas_invalidas += 1
                    continue
                
                nombre,precio,cantidad = fila
                
                try:
                    precio = float(precio)
                    cantidad =int(cantidad)
                    
                    if precio < 0 or cantidad < 0:
                        raise ValueError
                    
                    producto = {
                        'Nombre': nombre.strip(),
                        'Precio': precio,
                        'Cantidad': cantidad
                    }
                    
                    Productos_cargados.append(producto)
                except ValueError:
                    Filas_invalidas += 1
                    
    except FileNotFoundError:
        print('No encontrado')
        return inventario_memoria
    except UnicodeDecodeError:
        print('Problema de codificacion')
        return inventario_memoria
    
    opcion = input('Desea sobreescribir el inventario actual? (S/N): ').strip().upper()
    
    if opcion == 'S':
        inventario_memoria = Productos_cargados
        accion = 'Reemplazo'
        
    else:
        nombres_existentes = {p['Nombre']: p for p in inventario_memoria}
        
        for produc in Productos_cargados:
            if produc['Nombre'] in nombres_existentes:
                existente = nombres_existentes[produc['Nombre']]
                existente['Cantidad'] += produc['Cantidad'] 
                
                if existente['Precio'] != produc['Precio']:
                    existente['Precio'] = produc['Precio']
            else:
                inventario_memoria.append(produc)
                
        accion = 'Fusion (Cantidad sumada y precio actualizado si cambió)'
        
    print('RESUMEN')
    print(f'Productos cargados: {len(Productos_cargados)}')
    print(f'Filas invalidas omitidas: {Filas_invalidas}')             
    print(f'Accion realizada: {accion}')
    
    return inventario_memoria     
                    
    