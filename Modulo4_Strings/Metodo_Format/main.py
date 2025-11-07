name = 'Eduardo'
last_name = 'Garcia'

#4 - format
#base = 'El nombre completo es: {name} {last_name}. Su edad es: {age}' #cada juego de llaves {} es un placeholder
#full_name = base.format(name, last_name, 30) #se usa el metodo format para formatear strings
#print(full_name)

# name = input('Ingresa tu nombre: ')
# last_name = input('Ingresa tu apellido: ')
# age = input('Ingresa tu edad: ')

# full_name = base.format(name, last_name, age)
# print(full_name)
#el metodo format nos deja definir nombres entre los juegos de llaves{}

base = 'El nombre completo es: {name} {last_name}. Su edad es: {age}. Active: {active}'
full_name = base.format(
    name=name, 
    last_name=last_name, 
    age=30, 
    active=True
    )
#asi esta mas claro que valor va en cada placeholder
#De este modo se pueden tratar valores de diferentes tipos sin necesidad de convertirlos a string
print(full_name)