"""
if<con"""

number1 = 10
number2 = 20
#se puden usar cuantas condiciones anidadas sean posibles pero no es recomendable usarlas mucho incluso evitarlas
if number1 >= 10:
    print(">>> Number1 es mayor igual a 10.")
    if number1 > number2:
        print(">>> Number1 es mayor a number2.")
    else:
        print(">>> Number1 NO es mayor a number2.")