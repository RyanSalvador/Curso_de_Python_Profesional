def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    if amount > balance:
        return None
    return balance - amount

options = { #tambien se pueden almacenar las funciones así en diccionarios
    'a': deposit,
    'b': withdraw
}
option = input('Ingresa una opción (a/b):')
balance = int(input('Ingresa tu balance: '))
amount = int(input('Ingresa tu cantidad: '))

default = lambda *args, **kwargs: 'Lo sentimos, opción NO valida.'
#para funciones basicas que no necesiten muchas operaciones y con resultados sencillos se usa lambda y cosas tan especificas
function = options.get(option, default)
total = function(balance, amount)
print(total)





#para funciones basicas 

"""
son funciones sin nombre
funciones lambda siempre son de una sola linea de codigo
lambda <parametros>: <body> #siempre retornan un valor
"""
#tambien se les puede asignar a una variable
#add = lambda number1, number2=0: number1 + number2 #no necesita 'return' ya que siempre devuelve el valor 
# add = lambda *args: sum(args) #aplica los mismos principios de los args

# print(add(10))
# print(add(10, 20, 50, 50, 1, 3))

#reiterando en el codigo anterior