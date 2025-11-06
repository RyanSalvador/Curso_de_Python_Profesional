courses = (
#      0          1         2        3           4        5 
    "Python", "Django", "Ruby", "Ruby on Rails", "MySQL", "MongoDB"
)
# var1 =courses[0]
# var2 =courses[1]
# var3 =courses[2]
# var4 =courses[3]
# var5 =courses[4]

#var1, var2, var3, var4, var5 = courses[0], courses[1], courses[2], courses[3], courses[4]
# _ los guiones bajos se usan para ignorar valores en el desempaquetado esto son convenciones de python en si
#var1, _, var3, var4, var5, _ = courses # Desempaquetado de tuplas ya que lo siguiente igual es una tupla y se puede simplemente llamar asi


# print(
#     var1,
#     var3,
#     var4,
#     var5  
# )
var1, var2, *sub_courses, _, last_value = courses #apartir de este patron se guardan los demas valores en una lista
print(
    var1,
    var2,
    sub_courses,
    last_value
)