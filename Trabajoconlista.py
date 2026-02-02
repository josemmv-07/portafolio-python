trabajadores = ["Ana", "María", "Antonio", "Miguel"]



trabajadores.append("Juan")

print(trabajadores)
print(len(trabajadores))
print(trabajadores[2])
print(trabajadores[-1])
print(trabajadores[0:3])
print(trabajadores[2:4])
del trabajadores[0]
trabajadores.remove("Juan")
print(trabajadores.index("Antonio"))


for a in trabajadores:
    print(a)