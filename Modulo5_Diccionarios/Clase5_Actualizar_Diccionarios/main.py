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
#user['name'] = 'Codigo' #actualizar lista['valor'] = 'nuevo valor'
#user['last_name'] = 'Facilito' #agregar nuevo valor

id = user.setdefault('id', 100) #intenta obtener el valor y sino lo encuenta lo añade con su valor

courses = user.get('courses', [])
courses.append('Ruby Rails')
courses.append('Rust')

user.update({ #con esto se pueden actualizar llaves y tambien agregar nuevas llavez, se pasa el arguento que es el diccionario
    'name': 'Código',
    'settings': None,
    'last_name': 'Facilito',
    'courses': courses
})

del user['courses'] #con del se pueden eliminar la llave y su valor
value = user.pop('settings') #es otra forma de eliminar y sacarlo o extraer
print(value) #value es otro diccionario

user.clear() #diccionario.clear se resetea y se quitan todos los valores

print(id)

print( len(user) ) #esto nos da cuantos pares de llaves con sus valores
print(user)