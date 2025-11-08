def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    if amount > balance:
        return None
    return balance - amount

# func1 = deposit #asi se almacena la funcion entera sin poner el parentesis sino se estaría llamando a la funcion 
# func2 = withdraw #igual sin poner parentesis

# print(type(func1)) comprobamos que efectivamente son funciones almacenadas en variables
# print(type(func2))

# print(func1(100, 20)) #aqui usamos las variables como su funciones almacenadas
# print(func2(100, 20))

#Siguiente ejemplo 
def default(*args, **kwargs):
    return '>>> Lo sentimos, opción NO valida' #cualquier otra opcion  o nombres de opciones se vayan a este resultado

options = { #tambien se pueden almacenar las funciones así en diccionarios
    'a': deposit,
    'b': withdraw
}

option = input('Ingresa una opción (a/b):')
balance = int(input('Ingresa tu balance: '))
amount = int(input('Ingresa tu cantidad: '))

function = options.get(option, default)
#print(function
total = function(balance, amount)
print(total)