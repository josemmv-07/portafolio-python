""" Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo
 y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos
 y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa 
 que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será 
 enviado."""

payaso = 112
muñeca = 75



while True:
    pro = input("Para salir de este programa di [Q]\n"
                "Para calcular el peso total Payaso di [P]\n "
                "Para calcular el peso total de muñeca di [M]\n")
    if pro == "Q":
        break
    elif pro == "P":
        paya = int(input("Dime el número de payaso\n"))
        pt = payaso * paya
        print(f"El número de payaso son {paya} en total su peso es de {pt} g que en Kilogramos son {pt / 1000} Kg")
    elif pro == "M":
        muñe = int(input("Dime el número total de muñeca\n"))
        mt = muñeca * muñe
        print(f"El número de muñeca son {muñe} en total su peso es de {mt} g que en kilogramos son {mt / 1000} Kg")