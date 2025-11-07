# clave(llave) : valor
#String, tuplas, int, floar, booleans, func
# keys, values, items
#list(), tuple()

user = {
    'name': 'Cody',
    'age': 10,
    'active': True,
    'courses': [
        'Python', 'Django', 'Redis'
        ],
    'settings': (123, True),
}

print(
    #user.keys() nos da todas las llaves del diccionarios
    #list(user.keys()) crea una lista con los valores
    tuple(user.keys()) #crea una tupla con los valores
)

print(
    list(user.values()) #trae todos los valores la lista, tupla, etc
)

print(
    list(user.items()) #lista de tuplas con los pares llave y valor
)