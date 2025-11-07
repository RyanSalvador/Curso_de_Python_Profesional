# continue - break
# palabras reservadas sirven en for-each & while
# continue se salta a la siguiente iteracion
# break en cuanto se cumple se detiene el for o while

for number in range(1, 101):

    if number % 2 == 0 : #si es un numbero par

        continue
    if number == 99:
        break

    print(number)

