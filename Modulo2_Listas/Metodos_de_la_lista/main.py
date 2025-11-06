#               0        1        2        3        4
#             -5        -4        -3       -2        -1
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] #strings
new_courses = ["NodeJS", "Express", "PostgreSQL"]

courses.append("Ruby on Rails") #Agrega un elemento al final de la lista 
courses.append("PHP")
courses.append("Laravel")  

courses.insert(0, "JavaScript") #Agrega un elemento en la posicion indicada
courses.insert(2, "Java")
courses.insert(4, "C#")

courses.extend(new_courses)  #Agrega multiples elementos al final de la lista

""" print(
    "Python" in courses  #Verifica si un elemento existe en la lista con in
)

print(
    courses.index("Python")  #Devuelve el indice del elemento indicado tener cuidado porque sino existe lanza un error de preferencia condicionarlo
)
 """
courses.remove("Python")  #Elimina el primer elemento que coincida con el valor indicado
courses.remove("Django")

last_element =courses.pop()  #Elimina el ultimo elemento de la lista esto tambien lo devuelve como valor courses.pop() lo expulsa y lo retorna
first_element = courses.pop(0)  #Elimina el elemento en la posicion indicada y lo retorna

courses.clear()  #Elimina todos los elementos de la lista dejandola vacia

print(first_element)
print(last_element)

print(courses)
print(len(courses))


