#Docstrings
#un docstring es un comentario que se encuentra en la primera linea del cuerpo de la funcion
#explica exactamente como funciona nuestra funcion
#REVISAR QUE ESTANDARES UTILIZA TU EMPRESA 
#El que se muestra es estilo google 

def full_name(first_name, last_name):
    """Permite generar un nombre completo.
    
    Args:
        - first_name (String)
        - last_name (String)

    Return:
        String
    """
    return f'{first_name} {last_name}'

print(
    full_name.__doc__
)
#esto se pone en consola y se puede consultar la info
# >>> python3
# >>> from main import full_name
# >>> help(full_name)

