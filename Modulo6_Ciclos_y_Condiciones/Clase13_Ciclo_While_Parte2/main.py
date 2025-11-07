#juego numero magico
from random import randint #mandamos a llamar el modulo random para generar numeros aleatorios

number = None
random_number = randint(0, 20) #con esto podemos obtener un valor diferente cada vez en este rango designado
hits = 0

while number != random_number and hits < 3:
    number = int(
        input('Ingresa un número del 0 al 20: ') #str convertido a entero
    )
    if random_number > number:
        print('El número aleatorio es mayor.')
    else:
        print('El número aleatorio es menor.')
    hits += 1
else:
    if number == random_number:
        print(f'>>>Felicidades, encontraste el número. {random_number}')
    else:
        print(">>> Lo sentimos, no encontrate el número.")