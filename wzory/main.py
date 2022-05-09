#Pole kwadratu
x = int(input("podaj długość boku: "))

if x > 0:
    result = x * x
    print("pole wynosi:")
    print(result)
else:
    print("Bok nie może być ujemny!!")

#Pole trójkąta

x = int(input("podaj długość podstawy: "))
y = int(input("podaj wysokość: "))

if x > 0 and y > 0:
    result = 0.5 * x * y
    print("pole wynosi:")
    print(result)
else:
    print("Bok nie może być ujemny!!")

#Pole trapezu z małym easter eggiem B)

x = int(input("podaj długość dolnej podstawy:"))
y = int(input("podaj długość górnej podstawy:"))
z = int(input("podaj wysokość:"))

if x > 0 and y > 0 and z > 0:
    if x == 69 and y == 69 and z == 69:
        print("mmmm jebanko B)")
    else:
        result = 0.5 * (x + y) * z
        print("pole wynosi:")
        print(result)
else:
    print("Bok nie może być ujemny!!")