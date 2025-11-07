"""
if<condition>:
    ...
else:
    ...   
"""

color = 'Azul'

if color == 'Verde':
    print('>> Puedes continuar...')

elif color == 'Amarillo':
    print('>>> Alto parcial.')

elif color == 'Rojo':
    print('>>> Alto total.')

else: #Este else se ejecuta cuando ninguna de las condiciones anteriores en if o elif no se cumplieron
    print('!!! Lo sentimos, el color no es valido.')