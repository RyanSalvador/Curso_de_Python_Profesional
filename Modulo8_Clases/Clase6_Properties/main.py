class User:

    def __init__(self, username, password, email=None, rol ='Organizer'): #se usa por convencion el self para hacer referencia a el mismo
        self.username = username
        self._password = password #Private
        self.email = email 

        self.rol = rol

    @property #añadir propiedades 
    def password(self):
        if self.rol == 'Admin':
            return self._password
        return None
    
    @password.setter #permite la escritura el setter a diferencia del anterior
    def password(self, new_password):
        if self.rol == 'Admin':
            self._password = new_password

user1 = User(
    username='CodigoFacilito',
    password='password123',
    rol = 'Admin'
) 

user1.password= 'New password'
print(
    user1.password
)