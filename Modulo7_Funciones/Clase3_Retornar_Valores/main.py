""" palabra reservada snake_case
los parametros son opcionales, es necesario pasar la cantidad de argumentos que necesite la funcion
Se puede usar el return para cortar las funciones en ciertos momentos.
def <nombre_de_la_func.> (<parámetros, >):
    ...
"""
#no usar prints en funciones  mas de 1 accion
def multiply(number1, number2):
    result = number1 * number2
    return result #aqui termina la funcion al usar el return no importan las lineas de codigo de abajo y devuelve el valor

def full_name(first_name, last_name, prefix):
    full_name = f'{prefix} {first_name} {last_name}'
    return full_name


# result = multiply(10, 20)

# print(result-10)

user_full_name = full_name('Eduardo','Garcia', 'Mr')
print(
    f'Hola, el nombre del usuario es: {user_full_name}'
)

def division(number1, number2):
    if number1 == 0 or number2 ==0:
        return None
    return number1 / number2

print(
    division(10, 0)
)