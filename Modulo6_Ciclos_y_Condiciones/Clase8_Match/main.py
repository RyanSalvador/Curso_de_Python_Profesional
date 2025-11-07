#desde el 3.10 de python se agrega el match es un switch
# este | es un OR en python

score = 10

match score:
    case 10:
        print("Muchas felicidades, tu calificación es 10.")
    case 9 | 8:
        print("Felicidades, tu calificación es aprobatoria.")
    case 6 | 7:
        print("Aprobaste la material.")
    case _: #este es el ultimo casi por defecto
        print("Lo sentimos, calificación No aprobatorio")