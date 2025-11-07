# Entrada
# * (Posición) . (tuple)
# ** (Nombres) - (dictionary)


def show_info(**user):
    for key, value in user.items():
        print(key, '-', value)


show_info(
   username='cody',
   email='cody@codigofacilito.com',
   password='1234',
   active=True,
   courses=['Python', 'Django','Flask'],
   last_login='2025',
   is_super_user=True
)