class User:

    def __init__(self, username, password, email=None): #se usa por convencion el self para hacer referencia a el mismo
        self.username = username
        self.password = password
        self.email = email

user1 = User('Cody', 'password123', 'cody@codigofacilito.com') #por porsicion o por nombre
user2 = User(
    username='Cody2', 
    password='2password123', 
)
print(user1.username)
print(user1.password)
print(user1.email)

print(user2.username)
print(user2.password)
print(user2.email)