"""
La funciones en python puede devolver valores.
las funciones en python pueden tener parámetros/argumentos
las funciones tambien se le dominas metodos

utilidaded
* Reutilización de código( cuando sea nescesario o si es necesario)
* Dividir el código en bloques de código lógicos
* simplificar (aclarar) el código del proigrama

Dos tipo de funciones esta las predefinidas = print()....
Propias 

sintaxis
*def nombre_funcion():
-c intrucciones de la función 
-return(opcional)

*def nombre_funcion(parámetros)
- intrucciones de la función
- return(opcional)
ejecución
nombre_funcion()
nombre_funcion(parametro)

"""
def imprimeMensajes(): # definición (creación) de la función 
    
    print("Esto es un curso de Python")
    print("El curso acaba de empezar")
    print("El curso tendrá más de 1500 vídeos")
    print("La anterior línea era broma")

imprimeMensajes() # Llamada/invocación de la función

print("El programa ha terminado su ejecución")

def imPri():

    return "Este es el mensaje de la función" # devolver un valor solo puede uno 

print(imPri())

valorMensaje = imPri()
print(valorMensaje)

def imprimeMensajePersonalizado(mensaje, valor1, valor2):   # parametro o argumento

    return mensaje + str((valor1 + valor2)) # solo se puede llamar desde la función 

print(imprimeMensajePersonalizado("La suma es ", 5, 7)) # se almacena por el orden de la llamada 
 



