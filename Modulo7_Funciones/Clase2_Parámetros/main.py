""" palabra reservada snake_case
los parametros son opcionales, es necesario pasar la cantidad de argumentos que necesite la funcion

def <nombre_de_la_func.> (<parámetros, >):
    ...
"""
#             Parametro
def count_to(number):


    for n in range(1, number + 1):
        print(n)

def multiply(number1, number2):
    result = number1 * number2
    print(f'El resultado de la operación es: {result}')

def full_name(first_name, last_name, prefix):
    full_name = f'{prefix} {first_name} {last_name}'
    print(full_name)

#count_to() errado porque no tiene ningun parametro o en este caso se llama argumento

count_to(10) #siempre que llamemos debemos pasar un valor que se le llamará argumento
multiply(10, 20) #se asingan por posicion el pimero argumento al primer parametro
full_name(
    'Eduardo',
    'Garcia',
    'Mr'
)