#los diccionarios clave : valor son estructuras de datos que permiten almacenar pares de datos relacionados. Cada clave es única y se utiliza para acceder a su valor correspondiente. clave o llave
# Stringm tuplas, int, float, booleans inmutables
#la mayoria de los casos se usan strings como claves

user = {
    'name': 'User1',
    'age': 10,
    'active': True,
    'courses': [
        'Python', 'Django', 'Redis'
        ],
    'settings': (123, True),
    'name': 'User2', #sobreescribe el valor de la clave 'name'
    'name': 'User3' #sobreescribe el valor de la clave 'name'
}
print(user)
