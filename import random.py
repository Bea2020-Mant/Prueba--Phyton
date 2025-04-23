import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinanza de números!")
    print("Estoy pensando en un número entre 1 y 100.")

    while not adivinado:
        try:
            experimento = int(input("Adivina el número: "))
            intentos += 1

            if experimento < numero_secreto:
                print("El número es mayor.")
            elif experimento > numero_secreto:
                print("El número es menor.")
            else:
                adivinado = True
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Llamar a la función para iniciar el juego
juego_adivinanza()

