#               0        1        2        3        4
#             -5        -4        -3       -2        -1
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] #strings

courses[0] = "Ruby on Rails"  #modificamos el primer elemento de la lista
courses[1] = "MySQL" #modificar el elemento 

print(
    len(courses)   #la funcion len() nos devuelve la cantidad de elementos en una lista
)


value = courses[len(courses) - 1]  #len(courses) - 1 nos da el indice del ultimo elemento de la lista

print(
    value
)

value = courses[0] #los indices negativos empiezan a contar desde el final de la lista Esta es la forma mas python de buscar en listas

print(
    value
)