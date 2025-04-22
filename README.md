# Declarar variables
#nombre = input("¿Cuál es tu nombre? ")
#edad = int(input("¿Cuál es tu edad? "))

# Imprimir saludo
#Beprint(f"Hola {nombre}, tienes {edad} años.")

#def saludar(nombre):
 #   print (f"¡Hola, {nombre}! Bienvenida al taller.")
#saludar (nombre)

#for recorre in range(1,10):  # Imprime del 0 al 9
    #print(recorre)

def es_mayor_de_edad(edad):
    if edad >= 18:
        return "Es mayor de edad"
    else:
        return "Es menor de edad"

# Solicita la edad al usuario
edad = int(input("¿Cuál es tu edad? "))

# Llama a la función e imprime el resultado
print(es_mayor_de_edad(edad))

