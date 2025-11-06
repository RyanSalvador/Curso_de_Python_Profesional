#               0        1        2        3        4
#             -5        -4        -3       -2        -1
#[start:end] no se toma en cuenta el elemento de la posición "end"
#Es factible usar [:end] o [start:] se pueden usar para omitir el inicio o el final respectivamente
#slicing [::2] salta de 2 en 2
#Slicing es la capacidad de partir una lista en sub-listas

courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] #strings

new_list = courses [0:3]
print(new_list)  # ['Python', 'Django', 'Flask']
courses_copy = courses[:]  #Copia de la lista completa se le dice shallow copy

new_list_inverted = courses[::-1]  #Invierte la lista