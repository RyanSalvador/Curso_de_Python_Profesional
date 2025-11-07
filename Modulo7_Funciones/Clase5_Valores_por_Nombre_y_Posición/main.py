""" palabra reservada snake_case
los parametros son opcionales, es necesario pasar la cantidad de argumentos que necesite la funcion

def <nombre_de_la_func.> (<parámetros, >):
    ...
"""

def full_name(first_name, last_name, prefix):
    full_name = f'{prefix} {first_name} {last_name}'
    return full_name

print(
    full_name( #se puede poner los nombres de los parametros
        prefix='Mr.',
        first_name='cody',
        last_name='Facilito'
    )
)

print(
    full_name(
        'Eduardo',
        'Garcia',
        'Mr.'
    )
)
#igual se puede usar mixto