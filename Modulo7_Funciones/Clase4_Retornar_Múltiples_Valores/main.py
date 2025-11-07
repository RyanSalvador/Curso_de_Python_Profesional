""" palabra reservada snake_case
los parametros son opcionales, es necesario pasar la cantidad de argumentos que necesite la funcion

def <nombre_de_la_func.> (<parámetros, >):
    ...
"""

def foo():
    return 'Cody', True, 12 #Tupla no se devuelven varios valores solo 1 tupla

username, active, age = foo() #se usa el desempaquetado de tuplas
print(username, age) #aqui estan ya almacenados los valores que la funcion retorna