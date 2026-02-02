a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vocales = ["a", "e", "i", "o", "u"]
frase = "Hola, hoy estoy aprendiendo Python"
vocales_encontradas = 0

for item in a:
    print(item)

for letra in frase:
    if letra in vocales:
        print(f"He encontrado una '{letra}'")
        vocales_encontradas += 1

print(f"Vocales encontradas: {vocales_encontradas}")

numero_de_repe = int(input("Cuantas veces quieres repetir el mensaje?\n"))

for a in range(1,numero_de_repe + 1):
    print("Hola")