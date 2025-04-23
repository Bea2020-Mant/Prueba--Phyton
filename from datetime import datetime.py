from datetime import datetime

# Diccionario de menús por tiempo de comida
menu = {
    "desayuno": ["Tostadas con aguacate", "Avena con fruta", "Huevos revueltos con pan"],
    "comida": ["Pollo a la plancha con arroz", "Pasta al pesto", "Ensalada de quinoa"],
    "merienda": ["Yogur con granola", "Fruta picada", "Sándwich pequeño"],
    "cena": ["Sopa de verduras", "Pescado al horno", "Tortilla española"]
}

# Obtener hora actual
hora_actual = datetime.now().hour

# Determinar momento del día
if 6 <= hora_actual < 11:
    momento = "desayuno"
elif 12 <= hora_actual < 15:
    momento = "comida"
elif 16 <= hora_actual < 18:
    momento = "merienda"
elif 19 <= hora_actual < 22:
    momento = "cena"
else:
    momento = None

# Lógica de elección
if momento:
    print(f"\n ¡Es hora de {momento}! Elige uno de estos platos:")

    opciones = menu[momento]
    for i, plato in enumerate(opciones, start=1):
        print(f"{i}. {plato}")

    # Solicitar elección del usuario
    try:
        eleccion = int(input("Escribe el número de tu elección: "))
        if 1 <= eleccion <= len(opciones):
            print(f"\n Has elegido: {opciones[eleccion - 1]}. ¡Buen provecho! ")
        else:
            print(" Opción inválida. Intenta nuevamente.")
    except ValueError:
        print(" Por favor ingresa un número válido.")
else:
    print("\n No es hora típica de comida. ¡Toma agua o un snack saludable! ")
