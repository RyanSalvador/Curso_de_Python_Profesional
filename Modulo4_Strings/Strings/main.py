message = "Hola mundo!"


print(message)
print(type(message))
print(len(message))  # longitud del string

print("!" in message)  # True
print( message.index("!") ) # 
print( message[-2])

message2 = "h" + message[1:] #los strings son inmutables
print(message2)
#los strings son solo para lectura no se pueden modificar