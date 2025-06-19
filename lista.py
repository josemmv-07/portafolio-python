vocales = ["a", "e", "i", "o", "u"] # Creamos una lista
print(vocales[0])  

vocales.append("hola") # Añadimos una ultima a la lista
print(vocales[5])

vocales.pop() # Borramos la ultima de la lista 
print(len(vocales))

letra = "f"

print(letra in vocales) # Miramos si (f) pertenece a la lista de vocales 

letra = "a"

print(letra in vocales) # True pertenece (a)

