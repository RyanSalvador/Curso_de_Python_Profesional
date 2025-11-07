# clave(llave) : valor
#String, tuplas, int, floar, booleans, func

user = {
    'name': 'Cody',
    'age': 10,
    'active': True,
    'courses': [
        'Python', 'Django', 'Redis'
        ],
    'settings': (123, True),

}
print('name' in user)
# user_name = user['name']
# print(user_name)

#user['password] usar solo corchetes solo si estamos seguros de que si existe
user_name = user.get('password', 'Lo siento, el valor no existe') #devuele el valor de una forma segura
print(user_name)


#se pueden modificar y añadir nuevas llaves a los diccionarios
user['last_name'] = 'facilito' #añadir si no existe
user['name'] = 'codigo' #actualizar si existe
print(user)