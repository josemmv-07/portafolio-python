misDatos = ("Juan", 10, 9, 1997)

misDatosLista = list(misDatos)

print(misDatosLista)

misDatos1 = ["Jose", 10, 9, 1997]
misDatosTupla = tuple(misDatos1)
print(misDatosTupla)
nombre, dia, mes, agno = misDatosTupla

print("Jose" in misDatosTupla)
print(misDatosTupla.count("Jose"))
print(len(misDatosTupla))
print(mes)
print(nombre)
