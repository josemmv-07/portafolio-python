import os

titulo = " LISTA DE LA COMPRA "

print("\n" + titulo + "\n" + "_" * len(titulo) + "\n") 

lista = None
lista_de_la_compra = []

while lista != "Q":
    lista = input(" Que desea comprar? ([Q]) para salir\n")

    if lista != "Q":
        p = input(f"¿ Seguro que quiere añadir '{lista}'? (S/N)\n")

        if p == "S":
            lista_de_la_compra.append(lista)
            print(f"'{lista}' añadido!!\n")
        else:
            print(f"'{lista}' no se añadido \n")
    os.system("clear")

print("\nLa lista de la compra es: ")
print(lista_de_la_compra)