# zip
#sirve para unir iterables (listas, tuplas, etc) en una sola estructura de datos
#en si sirve para generar tuplas

users = ["user1", "user2", "user3"]
courses = ("Python", "Django", "Rails")
scores = [10, 8, 7]


response = list(zip(users, courses, scores))
print(response)  # <zip object at 0x104f5e680>