#spli -> lista
#join -> string


"""Split: Divide una cadena en una lista según un separador especificado.
courses = 'Python, PHP, Ruby, Django, MongoDB, Ruby on Rails'
list_courses = courses.split(', ')  # por defecto separa por espacios aqui se puso que fuera cada coma y espacio

print(courses  )
print(list_courses )
"""

#el metodo join permite generar un string a partir de una lista de strings
courses = ['Python', 'Ruby', 'Ruby on Rails', 'MongoDB' ]

message_couses = ' - '.join(courses) #une todos los elementos de la lista sin espacios aqui ponemos con que se unen
print(message_couses)
print(type(message_couses))
