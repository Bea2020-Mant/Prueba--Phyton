number1 = int(input("Inserta el numero 1: ")) 
number2 = int(input("Inserta el numero 2: "))

def sum(number1, number2):
    result = number1 + number2
    print(number1, "+", number2, "=", result)

def sub(number1, number2):
    result = number1 - number2
    print(number1, "-", number2, "=", result)

def mult(number1, number2):
    result = number1 * number2
    print(number1, "*", number2, "=", result)

def div(number1, number2):
    if (number2 != 0):
        result = number1 / number2
        print(number1, "/", number2, "=", result)
    else:
        print("El numero 2 es igual a 0 y no se puede dividir por 0")

# Llamadas a las funciones
sum(number1, number2)
sub(number1, number2)
mult(number1, number2)
div(number1, number2)
