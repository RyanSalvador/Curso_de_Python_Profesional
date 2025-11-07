# scope o alcance
# global - local
# las variables locales solo viven en su contexto y no pueden ser modificadas ni consultadas fuera

username = 'Cody' #Global

def show_info():
    username = 'Codigo Facilito' #Local

    #global username #sirve para poder mover cambiar esa variable global pero es una mala practica ya que puede afectar en otras zonas de codigo
    print(id(username))

show_info()
print(id(username))