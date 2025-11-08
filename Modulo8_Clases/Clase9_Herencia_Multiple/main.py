#herencia multiple 
#cando se busca un metodo intenta buscarlo dentro de la clase original y asi va avanzando
#desde izquierda a derecha y en cuanto lo encuentra lo ejecuta incluso primero en la case base
#intentar evitar que se sobreescriban metodos para saber con exactitud cual metodo estamos utilizando
class ClaseZ:
    def say_hello(self):
        print('>>> Hola Mundo, desde la clase Z!!!')
    
class ClaseA(ClaseZ):
    def say_hello(self):
        print('>>> Hola Mundo, desde la clase A!!!')

class ClaseB:
    def say_hello(self):
        print('>>> Hola Mundo, desde la clase B!!!')

    def say_goodbye(self):
        print('>>> Adios!')

class ClaseC(ClaseA, ClaseB):
    ...

c = ClaseC()
c.say_hello()
c.say_goodbye()