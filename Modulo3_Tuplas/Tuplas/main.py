#tuplas         0          1     2
#               -3       -2     -1 
settings = ("localhost", 3306, True,)

print(settings)
print(type(settings))  #las tuplas se definen con parentesis y son inmutables

print("-------")
# settings[0] = "198.2.168.0.1" #esto genera un error porque las tuplas son inmutables

print(settings[0])  #accedemos al primer elemento de la tupla
print(settings[1]) 
print(settings[2]) 