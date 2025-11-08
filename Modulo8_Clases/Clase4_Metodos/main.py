
class User:

    def __init__(self, username, password, email=None): #se usa por convencion el self para hacer referencia a el mismo
        self.username = username
        self.password = password
        self.email = email


    def say_hello(self): #Tambien se usa por convencion el self para hacerse referencia a si mismo
        print(
            '>>> Hola soy el usuario', self.username
        )
    
    def login(self, username, password):
        if self.username == username and self.password == password:
            self.say_hello()
            return True
        
        return False


user1 = User(
    'Cody',
    'password123'
) 

user1.login('Cody', 'password123')
   