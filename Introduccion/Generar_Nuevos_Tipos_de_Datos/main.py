# int - float estas son funciones para convertir tipos de datos
# al igual se pueden usar los str() y bool() para convertir a string y booleanos


first_name = input("Ingresa tu nombre: ") #str
age = int(input("Ingresa tu edad: "))#int
height = float(input("Ingresa tu altura: ")) #float
status = input("Tu usuario se encuentra activo? (yes/no) ") == "yes" #bool

print(first_name)
print(age)
print(height)
print(status)

print(type(first_name))
print(type(age))
print(type(height))
print(type(status))
