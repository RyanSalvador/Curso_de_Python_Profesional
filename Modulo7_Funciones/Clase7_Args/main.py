# Entrada
# * (Posición) . (tuple)
# ** (Nombres) 

def suma(*numbers):
    return sum(numbers)

print(
    suma(10, 20, 4, 5, 6, 7, 8)
)

def show_info(username, email, *scores):
    print(username)
    print(email)

    average = sum(scores) / len(scores)
    print(average)


show_info(
    'cody',
    'cody@codigofacilito.com',
    10, 10, 9 ,8, 9, 5 #tupla pensar siempre en que posicion se ponen
)