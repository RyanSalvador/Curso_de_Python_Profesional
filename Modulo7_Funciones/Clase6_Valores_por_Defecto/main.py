#Solo se pueden asignar por default de derecha a izquierda
#Si yo no pongo por default el ultimo valor no puedo poner en default el que está a su izquierda y sucesivamente


def calculate_total(price, tax=0.05, discount=0):#aqui se define por default el valor 0 en descuento por si no se proporcione
    total = price + (price * tax) - discount
    return total

total = calculate_total(100, 0.08, 10)
print('Total', total)

total = calculate_total(100, 0.08)
print('Total', total)

total = calculate_total(200)
print('Total', total)

#tambien sirve asi con nombres especificos

total = calculate_total(
    price=500,
    tax=0.02,
    discount=20
)
print('Total', total)