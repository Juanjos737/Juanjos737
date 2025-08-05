import time 
#medcicion de ejecucion con un While
inicio = time.time()
for i in range (5):
    print(i)
fin = time.time()
tiempofinal = fin - inicio 
print ("tiempo de ejecucion: ", tiempofinal)

contador = 0
while contador <= 10:
    print (contador)
    contador +=1

fin = time.time()
tiempofinal = fin - inicio

print ("tiempo de ejecucion ", tiempofinal)

#formas de controlar while
 
"""
Por numeros reales o enteros 
por booleanos
por cadenas de texto

no primitivos
listas
tuplas
diccionarios
sets
rangos
Arreglos: vectores y matrices 

"""

palabra = input ("Ingrese una palabra: ")
while palabra.upper() == "s":
    palabra = input ("Ingrese una palabra: ")
print ("Fin del ciclo while")