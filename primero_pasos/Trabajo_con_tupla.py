
# Tupla
misDatos = ("Jose", 10, 9, 1997)

print(misDatos)

# Copnvertir tupla a lista 
misDatosLista = list(misDatos)
print(misDatosLista)

# Convertir lista a tupla
mis = ["Jose", 5, 2, 1998]
mistupl = tuple(mis)

print(mistupl)

# saber si esta en la tupla

print(10 in misDatos)

# saber cuanta veces esta en la tupla 

print(misDatos.count("Jose"))

# saber la longitus de una tupla

print(len(misDatos))

# desempaquetado de tupla

nombre, dia, mes, agno = misDatos

print(nombre)