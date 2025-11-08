#funciones permiten recibir otras funciones estas se llaman de orden superior

def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    if amount > balance:
        return None
    return balance - amount

def handle_operation(callback, *args, **kwargs):
    print('>>>> Comenzamos operacion...')
    
    result = callback(*args, **kwargs)
    print('El resultado es: ', result)


options = { 
    'a': deposit,
    'b': withdraw
}
option = input('Ingresa una opción (a/b):')
balance = int(input('Ingresa tu balance: '))
amount = int(input('Ingresa tu cantidad: '))

default = lambda *args, **kwargs: 'Lo sentimos, opción NO valida.'

function = options.get(#funcion get funcion de orden superior
    option,
    lambda *args, **kwargs: 'Lo sentimos, opción NO valida.'
)

handle_operation(
    callback=function,
    balance=balance,
    amount=amount
)