# for-each & while
# range la funcion permite generar un rango de numeros enteros es una coleccion
# range(start, stop +1) desde donde hasta donde
# usar range solo si uso rangos de enteror y no indices

for number in range(10): # el rango es del 0 - 9 esto es al poner un solo argumento
    print(number)

for number in range (5, 10+1): #normalmente se pone +1 para declarar que si queremos el ultimo valor
    print(number)

print(">>>>>>>>>>>>>>>>>>>>")

number = [1, 2, 3, 4, 5]

for index in range( len(number)):
    print(number[index])


print(">>>>>>>>>>>>>>>>>>>>")

#Mas ejemplos
courses = ['Python', 'Go', 'Rust', 'Django', 'Java']

# for index in range( len(courses)):
#     print(courses[index]) NO ES NECESARIO YA QUE LA FUNCION FOR YA HACE HACE ESTO SIN USAR RANGE

for course in courses:
    print(course)