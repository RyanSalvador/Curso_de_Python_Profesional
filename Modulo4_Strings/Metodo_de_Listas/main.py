title = '    Curso profesional de Python!   '
title = title.strip()  # Elimina espacios en blanco al inicio y al final
print(title.strip())  # Elimina espacios en blanco al inicio y al final sirve para estandarizar entradas de usuario


print(title.upper())  # Convierte a mayúsculas
print(title.lower())  # Convierte a minúsculas prefiero este

print(title.find('p'))  # Encuentra la posición de la primera aparición de un carácter o subcadena en que indice
print(title[6]) # Accede al carácter en la posición indicada


print('6'.isnumeric()) # Verifica si el string intenta representar un número


#poner mayusculas
message = 'codigo facilito'
print(message.capitalize())  # Convierte el primer carácter a mayúscula y el resto a minúsculas

print(message[0].upper() + message [1:]) # Otra forma de capitalizar una cadena manualmente como se vio en otro ejemplo

print(f'{message[0].upper()}{message[1:]}') #Usando f strings para capitalizar manualmente una cadena