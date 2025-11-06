# esto es para poner comentarios en Python. solo para la misma linea
"""Esto es un comentario de 
multiplen lienas de de codigo en python
"""
"""
print("Hola mundo, desde un scrip en Python.")
"""


#<variable> = <valor> # Asignacion de variables no hay que definir el tipo de dato es de tipado dinamico
"""
name = "codigo Facilito" # string
print(name)
print(type(name))
type(name) # para saber que tipo de dato es la variable
"""
#Para nombrar en python se usa snake_case siempre unir todo con guiones bajo y todo en minusculas

#string Se pueden usar comillas simples o dobles

#integers numeros enteros positivos o negativos, si se tienen numeros grandes 100_000_000 se pueden usar guiones bajos para mejorar la lectura

#Floats Se usan para numeros decimales 
#Booleans verdadero o falso True o False

#En python no existen las constantes como en otros lenguajes, pero se puede usar convencion de poner el nombre de la variable en mayusculas para indicar que no debe cambiar su valor
# PI = 3.1416
#en las operaciones por defecto el / siempre dará un float aunque los numeros sean enteros si quiero que de un numero entero se debe usar el //
number = 10
result = number / 10 #float
print("El resultado es:", result)

number2 = 10
result2 = number2 // 10 #integer
print("El resultado es:", result2)