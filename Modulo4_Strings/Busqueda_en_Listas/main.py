title = 'Curso profesional de Python!'

#print( title.upper())   #Genera un nuevo string en mayusculas

#print(title.lower())    #Genera un nuevo string en minusculas
print(
    'curso' in title.lower()
)

print(
    title.count("Curso") #inclusive unicamente letras
)

print(
    title.startswith('Curso')
)

print(
    title.endswith('!')
)