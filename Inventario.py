def control_inventario():
    # Paso 1: Solicitar inventario inicial
    inventario = int(input("Ingresa la cantidad inicial de pares de zapatos en la tienda: "))
    
    # Validar que el inventario sea mayor a 0
    if inventario <= 0:
        print("El inventario inicial debe ser mayor que cero.")
        return

    transacciones = 0

    # Paso 2: Bucle para ventas hasta que inventario sea 0
    while inventario > 0:
        print(f"\nInventario actual: {inventario} pares")
        venta = int(input("¿Cuántos pares de zapatos se vendieron? "))

        if venta <= 0:
            print("Por favor ingresa un número positivo.")
            continue
        if venta > inventario:
            print(f"No puedes vender más pares de los que tienes. Solo quedan {inventario}.")
            continue

        inventario -= venta
        transacciones += 1

    # Paso 3: Reportar resultado
    print(f"\n¡Inventario agotado! Total de transacciones realizadas: {transacciones}")

# Ejecutar el programa
control_inventario()
