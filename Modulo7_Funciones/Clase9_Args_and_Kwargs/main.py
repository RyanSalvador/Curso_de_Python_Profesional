# Entrada
# * (Posición) . (tuple)
# ** (Nombres) - (dictionary)
# Por convencion de python se llaman *args y **kwargs
# No es una regla pero se usa así
"""
def show_info(*args, **kwargs):
    print('>>> Info')
    for value in args:
        print(value)
    
    print('\n')
    print('>>> Details')
    for key, value in kwargs.items():
        print(key, value)

show_info(
    'Cody', 'Facilito', 12, 'cody@codigofacilito.com',
    courses= ['Python', 'Flask', 'Django'],
    score=10,
    active=True,
    is_super_admin=True
)
"""

def show_info(username, last_name, *args, active=True, is_super_admin=False, **kwargs):
    print("Username", username)
    print("Last Name", last_name)

    print('>>> Extra info: ')
    for value in args:
        print(value)
    
    print("Active", active)
    print("Super Admin", is_super_admin)
    print(kwargs)

show_info(
    'Cody', 'Facilito',
    'info@codigofacilito.com', 'password123', #args
    courses=['Python', 'Flask'], is_deleted=False #kwargs
)
