#for-each & while
""" La condicion while ejecutara hasta que su condicion cambie
usar si y solo si no sabemos cuantas veces se va iterar
while <condition>:
    ...
"""

# counter = 0

# while counter < 10:
#     print('Valor:', counter)
#     #counter = ocuenter + 1
#     counter += 1 #esta es la forma mas pythonica

# for number in range (0, 10): #lo mismo de arriba pero siendo lo mas coherente si sabemos cuantas veces queremos iterar
#     print(number)

counter = 0
number = int(
    input('Ingresa un número.')
)

while number > 0:
    number = number // 10 #en esta operacion se recorre el punto hacia la izquierda y podemos saber la cantidad de digitos
    counter += 1
else:
    print("La cantidad de dígitos de tu número es:", counter) #cuando deje de ejecutarse el while se ejecuta el else