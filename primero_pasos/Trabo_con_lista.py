trabajadores = ["Ana", "María", "Antonio", "Miguel"]

print(trabajadores)

print(len(trabajadores))
# añadir

trabajadores.append("Juan")
print(trabajadores)

print(trabajadores[2])
print(trabajadores[-1])
print(trabajadores[-5])

print(trabajadores[0:3])
print(trabajadores[2:3])
# borrar elemento indicando el índice
del trabajadores[4]
print(trabajadores)

trabajadores.append("Juan")
print(trabajadores)

# Elimina un elemento indicando valor

trabajadores.remove("Juan")
print(trabajadores)

#la función index, permite averigua el ínice de un elemento

print(trabajadores.index("Ana"))
#la función count nos permite saber cuántas veces aparece un mismo elemeto en una lista

print(trabajadores.count("Ana"))