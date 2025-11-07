# ciclos
# for-each & while
#for each terminara hasta que se itere hasta el ultimo de los valores de las colecciones

numbers = [20, 5, 6, 15, 25] #pueden ser listas,tuplas
message = 'Hola mundo' #ejemplo con strings
user = {
    'name': 'Eduardo',
    'age': 31,
    'password': 'password123'
}

""" permite iterar
for <variable> in <collection>:
    ...
"""
for number in numbers:
    print('El valor de la variable es :', number)


for caracter in message: #strings
    print(caracter)


print(user.items()) #esto da 2 valores y por eso se usan 2 variables para que se asignen en pares.
for key, value in user.items(): #aqui desempaquetamos la tuplas en el mismo for
    print("La llave es", key, "el valor es:", value)
