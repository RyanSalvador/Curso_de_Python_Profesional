#               0        1        2        3        4
#             -5        -4        -3       -2        -1
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] #strings

# copy
# reverse
# sort

copy_list = courses.copy()  #Crea una copia de la lista original igual que couses[:]
print(copy_list)

# reverse_list = courses[::-1]  #Crea una copia de la lista original pero invertida
#print(reverse_list)

reverse_list = courses.reverse()  #Invierte el orden de los elementos de la lista este metodo cambia la lista original
print(courses)