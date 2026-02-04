# No se puede remitir las claves 
lasCapitales = {"España":"Madrid", "Francia":"París", "Reino Unido":"Londres"}

print(lasCapitales)

# para agregar elementos

lasCapitales["Colombia"] = "Bogotá"

print(lasCapitales)

# si no hemos equivocado podemos cambiar el valor 

lasCapitales["España"] = "Málaga"
print(lasCapitales)

# Para eliminar clave 

del lasCapitales["España"]

print(lasCapitales)

datos = {"España":"Madrid", 23:"M Jordan", "Mosquetero":3}

print(datos)


# claves de un diccionario utilizando tuplas
clavesCapitales = ("España", "Reino unido", "Colombia", "Portugal")

capitalesMundo = {clavesCapitales[0]:"Madrid", clavesCapitales[1]:"Londres", clavesCapitales[2]:"Bogotá", clavesCapitales[3]:"Lisboa"}
print(capitalesMundo)

# como acceder a un elementos para saber el valor 

print(capitalesMundo["Colombia"]) 

#como saber las claves 
print(capitalesMundo.keys())

# saber valor
print(capitalesMundo.values())

# conocer las longitus
print(len(capitalesMundo))

# Diccionarios anidados 

datosJordan = {23:"Jordan", "Nombre":"Michael", "Equipo":"C Bulls", "anillos":{"Temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(datosJordan)

print(datosJordan["anillos"])
print(datosJordan.keys())
print(datosJordan)
