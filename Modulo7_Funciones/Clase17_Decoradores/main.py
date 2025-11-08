#decoradores
#es una funcion que permite añadir funcionalidad a otras funciones
#no modifica a la funcion original ayuda a hacer diferentes cosas sin cambiar

#A(B) -> C
#A (DECORADOR)
#B (FUNCION A DECORAR base)
#C (Funcion decorda base + nuevas lineas de codigo)
            # B
def decorator(func): #A

    def wrapper(*args, **kwargs): # C
        print('>>>> Antes del llamado')
        result = func(*args, **kwargs) #ahora pueden almacenar n cantidad de argumentos
        print('>>> Despues del llamado')
        return result
    
    return wrapper

@decorator
def hell_world():
    print('Hola mundo')

hell_world()

@decorator
def suma(number1, number2):
    return number1 + number2

print(suma(10, 20))