#Closures
#funcion anidada que tiene memoria
#funciones anidadas que recuerdan y pueden acceder a variables que fueron creadas dentro de su entorno

def multiply(number1): #Local (10)

    def operation(number2):
        return number1 * number2
    
    return operation


var1 = 10
func_operation = multiply(var1) #se llama y finaliza

Var1= 20
print('El resultado es: ')
result = func_operation(3) #aqui apesar de que se finalizó recuerda que valia 10 antes
print(result)