name = 'Eduardo'
last_name = 'Garcia'

#1
full_name = name + ' ' + last_name + str(30) #para añadir un numero entero a un string 
print(full_name)

#2
full_name = ' '.join([name, last_name]) #Se usa un espacio como separador se hace una lista con los strings a unir
print(full_name)

#3 (%s) se usa en los logs pero no se usa en los scrips convencionales
full_name = 'El nombre completo es: %s %s' % (name, last_name) #se usa el operador % para formatear strings
print(full_name)
