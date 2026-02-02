a = float(input("Dígame su peso en kg: "))
print("Su peso es: " + str(a) + " kg")

b = float(input("Dígame su estatura en m: "))
print("Su estatura es: " + str(b) + " m")

imc = a / (b * b)
print("Entonces su IMC es:", round(imc, 2))
