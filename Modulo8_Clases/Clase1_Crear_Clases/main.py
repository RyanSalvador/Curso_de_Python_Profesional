""" PascalCase se usa poco parentesis opcional al definir
class <NombreClase>(): 
    ...

<variable> = NombreClase()
Aqui ya es obligatorio el parentesis"""

class User:
    username = ''
    password = ''
    email = ''

user1 = User()
user2 = User()
user3 = User()

user1.username = 'cody'
user1.email = 'cody@codigofacilito.com'
user1.password = 'password123'

user2.username = 'cody2'
user2.email = 'cody2@codigofacilito.com'
user2.password = 'password123'

user3.username = 'cody3'
user3.email = 'cody3@codigofacilito.com'
user3.password = 'password123'

print(user1.username)
print(user1.password)
print(user1.email)

print(user2.username)
print(user2.password)
print(user2.email)


print(user3.username)
print(user3.password)
print(user3.email)


print(type(user1))