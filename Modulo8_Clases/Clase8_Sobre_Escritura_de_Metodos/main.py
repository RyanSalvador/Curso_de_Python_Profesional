class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False
    
class Admin(User):
    def __init__(self, username, password, email):
        super().__init__(username, password) #con esto EVITAMOS TANTO DUplicado de codigo
        # self.username = username
        # self.password = password
        self.email = email
    
    def send_mail(self):
        print('>>> Enviando correo a ', self.email)

    def login(self, username, password):
        #if self.username == username and self.password == password:
        if super().login(username, password): #igual para reducir codigo duplicado
            self.send_mail()


class Organizer(User):
    ...

admin = Admin('Admin1', 'password', 'info@codigofacilito.com')
organizer = Organizer('Organizer1', 'password')
    

print(admin.login('Admin1', 'password'))
print(organizer.login('Organizer1', 'password'))