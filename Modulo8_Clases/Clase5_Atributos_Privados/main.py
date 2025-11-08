#las anotaciones con guion bajo es privado pero es solo una convencion no es algo de python
#no existen las variables privadas en python

class User:

    def __init__(self, username, password, email=None): #se usa por convencion el self para hacer referencia a el mismo
        self.username = username
        self._password = password #Private por convencion 
        self.__email = email #doble guion bajo  (Name Mangling) aqui se podria ver si se cambiaron los atributos se guarda el original con un_ al inicio

user1 = User(
    'Cody',
    'password123'
) 
user1._password = 'Cambio de contraseña'
print(user1._password) #python permite cambiar y consultar tener mucho ojo


user1.__email = 'cambio de valor'


print(
    user1.__dict__)