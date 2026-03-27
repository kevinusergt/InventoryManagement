import csv  # Importa el módulo para trabajar con archivos CSV

def guardar_CSV(inventario,ruta,Incluir_Header=True):
    
    try:
        # Abre el archivo en modo escritura
        with open(ruta, 'w') as datos:
            Wr = csv.writer(datos)  # Crea el objeto escritor CSV
            
            # Si se desea, escribe la fila de encabezados
            if Incluir_Header:
                Wr.writerow(['Nombre','Precio','Cantidad'])
            
            # Recorre cada producto del inventario y lo escribe en el archivo
            for producto in inventario:
                Wr.writerow([
                    producto['Nombre'],
                    producto['Precio'],
                    producto['Cantidad']
                ])    
        print(f'Inventario guardado en:{ruta}')
    
    # Manejo de cualquier error inesperado
    except Exception as e:
        print(f'Error inesperado: {e}')        
                    


def cargar_CSV(ruta, inventario_memoria):
    Productos_cargados =[]  # Lista temporal para almacenar productos válidos
    Filas_invalidas = 0     # Contador de filas con errores
    
    try:
        # Abre el archivo en modo lectura
        with open(ruta,"r",newline='') as file:
            carga = csv.reader(file)  # Lector CSV
            
            # Lee el encabezado
            encabezado = next(carga,None)
            
            # Verifica que el encabezado sea correcto
            if encabezado != ['Nombre','Precio','Cantidad']:
                print('Error, encabezado invalido. Debe ser: Nombre, Precio, Cantidad')
                return inventario_memoria
            
            # Recorre cada fila del archivo
            for fila in carga:
                
                # Valida que tenga exactamente 3 columnas
                if len(fila) != 3:
                    Filas_invalidas += 1
                    continue
                
                nombre,precio,cantidad = fila
                
                try:
                    # Convierte los datos a tipos correctos
                    precio = float(precio)
                    cantidad =int(cantidad)
                    
                    # Valida que no sean valores negativos
                    if precio < 0 or cantidad < 0:
                        raise ValueError
                    
                    # Crea el producto como diccionario
                    producto = {
                        'Nombre': nombre.strip(),
                        'Precio': precio,
                        'Cantidad': cantidad
                    }
                    
                    # Agrega el producto válido a la lista
                    Productos_cargados.append(producto)
                
                # Si hay error en conversión o validación
                except ValueError:
                    Filas_invalidas += 1
                    
    # Manejo de archivo no encontrado
    except FileNotFoundError:
        print('No encontrado')
        return inventario_memoria
    
    # Manejo de errores de codificación
    except UnicodeDecodeError:
        print('Problema de codificacion')
        return inventario_memoria
    
    # Pregunta al usuario si desea reemplazar o fusionar
    opcion = input('Desea sobreescribir el inventario actual? (S/N): ').strip().upper()
    
    # Reemplaza completamente el inventario
    if opcion == 'S':
        inventario_memoria = Productos_cargados
        accion = 'Reemplazo'
        
    else:
        # Crea un diccionario para acceso rápido por nombre
        nombres_existentes = {p['Nombre']: p for p in inventario_memoria}
        
        # Fusiona productos
        for produc in Productos_cargados:
            if produc['Nombre'] in nombres_existentes:
                existente = nombres_existentes[produc['Nombre']]
                
                # Suma cantidades
                existente['Cantidad'] += produc['Cantidad'] 
                
                # Actualiza precio si cambió
                if existente['Precio'] != produc['Precio']:
                    existente['Precio'] = produc['Precio']
            else:
                # Agrega producto nuevo
                inventario_memoria.append(produc)
                
        accion = 'Fusion (Cantidad sumada y precio actualizado si cambió)'
        
    # Muestra resumen de la operación
    print('RESUMEN')
    print(f'Productos cargados: {len(Productos_cargados)}')
    print(f'Filas invalidas omitidas: {Filas_invalidas}')             
    print(f'Accion realizada: {accion}')
    
    return inventario_memoria      
                    
    