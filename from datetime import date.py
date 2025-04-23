from datetime import date

# Paso 1: Pedir nombre y año de nacimiento
nombre = input("¿Cuál es tu nombre? ")
anio_nacimiento = int(input("¿En qué año naciste? "))

# Paso 2: Calcular edad
anio_actual = date.today().year
edad = anio_actual - anio_nacimiento

# Paso 3: Mostrar resultado
print(f"Hola {nombre}, tienes aproximadamente {edad} años.")
