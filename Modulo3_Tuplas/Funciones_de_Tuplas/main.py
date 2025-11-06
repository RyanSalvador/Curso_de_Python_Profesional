numbers = (
    1, 4, 5, 3, 3, 7, 2, 10
)

print(
    len(numbers) #retorna el numero de elementos de la tupla
)

print(
    #sorted(numbers) #retorna una lista ordenada en ascendente
    sorted(numbers, reverse=True) #retorna una lista ordenada en descendente
)

print(
    numbers.count(1) #retorna el numero de veces que aparece un elemento en la tupla en caso de no existir devuelve 0 se puede saber si esta en la tupla
)

# True -> 1 lo reconoce como el numero 1
print(
    3 in numbers #retorna True si el elemento esta en la tupla o False si no esta
)

print(
    numbers.index(7) #retorna el indice de la primera aparicion del elemento en la tupla en caso de no existir lanza un error
)