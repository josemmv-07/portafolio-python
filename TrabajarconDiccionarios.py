

lasCapitales = {"España":"Madrid", "Francia":"Toulousse", "Reino Unido":"Londres"} # España Clave : Madrid Valor

lasCapitales["Colombia"] = "Bogotá" # Añade
lasCapitales["Francia"] = "París" # Corrige 

print(lasCapitales)

del lasCapitales["Reino Unido"] # Borra 

print(lasCapitales)

datos = {"España":"Madrid", 23:"M Jordan", "Mosqueteros":3}
print(datos)

clavecapitales = ("España", "Reino Unido", "Colombia", "Portugal")

capitalesMundo = {clavecapitales[0]:"Madrid", clavecapitales[1]:"Londres", clavecapitales[2]:"Bogotá", clavecapitales[3]:"Lisboa"}
print(capitalesMundo["Colombia"])
print(capitalesMundo.keys()) # Las claves
print(capitalesMundo.values()) # Los valores
print(len(capitalesMundo)) # Longitud


datosJordan = {23:"Jordan", "Nombre":"Michael", "Equipo":"C Bulls", "anillos":{"Temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}

print(datosJordan["anillos"])
print(datosJordan.keys)
print(datosJordan)