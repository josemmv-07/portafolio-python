def saludo_secreto():
    print("Hola mundo")


    a = input("¿Cómo estás?")
    b = input("¿Dos más dos?")

    if b == "2":
        print("Tu si que sabes...")

def saludo_sectario(nombre):
    print(f"Hola {nombre[::-1]}")


saludo_sectario("jose")
saludo_sectario("María")


def largo_string(mi_string):
    largo = 0
    for n in mi_string:
        largo += 1
        return largo
    

largo_de_la_string = largo_string("Hola mundo")

print(largo_de_la_string)