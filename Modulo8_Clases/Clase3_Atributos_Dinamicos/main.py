#tener mucho cuidado porque se pueden seguir agregando mas instancias a la misma clase fuera de la misma
#evitar añadir atributos fuera de init
class User:

    def __init__(self, username, password, email=None): #se usa por convencion el self para hacer referencia a el mismo
        self.username = username
        self.password = password
        self.email = email

user1 = User(
    'Cody',
    'password123'
) 

user1.is_admin = True
user1.courses = [
    'Python', 'Django', 'Flask'
]

print(user1.is_admin)
print(user1.courses)
print(user1.__dict__) #asi podemos saber todo lo que contiene