#Introducción a Python.

#IMPORTANTISIMO: NO EXISTEN LAS CONSTANTES, Y LOS BLOQUES SE DEFINEN POR LA ALTURA DE LA SANGRIA

# print("-----------------")
# print("Hola mundo")

# '''
# Comentario en bloque
# Primera clase con Python
# '''
# #Comentario en línea

# apellido="Perez"
# nombre="Jorge"
# print("Apellido:", apellido, end=" ") #end="" es para que imprima todo en una sola línea
# print("Nombre:", nombre)

# #Ingresos de datos por un input---------------------------------------------------------------------------
# #let = input("Ingrese su nombre ")
# #print(let)
# #Esto mismo en una sola línea sería:
# #print(input("Ingrese su nombre: ") )

# #Tipos de datos
# varString = "Cadena de caracteres"
# varNum = 12345 #enteros
# varFloat = 12.5 #decimal
# varBool1 = True #Booleano
# varBool2 = False #Booleano

# #SUMA
# print("Resultado de una suma: ", 5+2)
# print("Menor : 5 < 10", 5 < 10)
# print("Mayor : 5 > 10", 5 >10)

# b = 6
# print(b<10)

# #Ponemos el 5 entre comillas para que lo tome como string (letras), pero lo tenemos que convertir a número entero con "INT", para convertir a decimal "FLOAT"
# a = "5"
# a = int(a)
# print(a<10)
# print(3 * (7 - b))
# c = None #se usa none cuando queremos crear una variable pero no tenemos definido un valor
# # let c; sería en javascrip
# print("A is none?", a is None)
# print("c is none?", c is None)

# #Sentencia IF--------------------------------------------------------------------------------
# edad = int(input("Ingrese su edad "))
# if edad > 18:
#     print("Es mayor de 18")
# else:
#     print("No es mayor de edad")
#     print("B tiene",b) #aca uso la variable b ya definida al principio (no tiene coherencia, es un ej nomás)

# b = "Mi nombre es roberto"
# print("B tiene: ",b)

# #Podemos inicializar una lista
# a = [1,2,3,4,5]

#while (mientras)--------------------------------------------------------------------------------
# print("Prueba while con incremento")
# contador = 0
# while True:
#     contador +=1
#     print(contador)
#     if contador==5 :
#         break #para cortar el ciclo
# print("Fin del programa")

#for ---------------------------------------------------------------------------------------------
#print("Prueba FOR con incremento")
n = int(input("Ingrese valor numérico "))
# #for cont in range(0,n+1,1): #range (inicio, fin, incremento)
#    #  print(cont) #la variable cont puede ser cualquier letra, en este caso con para referenciar a un contador

# #otra forma de hacer el for
# print("Otra forma de hacer el for")
# for cont in range (n):
#     print(cont+1)

#For definido como funcion, se imprime en cada nivel del bloque para mostrar su importancia de la altura en la que se escribe el código ¡¡IMPORTANTE!!!
def imprimir(n):
    """Documentación del módulo imprimir """
    for cont in range(n):
        print("Contador: ", cont+1)
    print("Dentro de la función")
print("Antes de llamar a la función")
imprimir(n)
print(imprimir.__doc__) #asi se imprimie el docstrings

#DOCSTRINGS: TIPO DE COMENTARIOS QUE SE USAN PARA DOCUMENTAR UN BLOQUE
# def suma(a, b):
#     """Esto es un doctrings, SE IMPRIME EN LA CONSOLA y sirve para explicar lo que va a suceder en esta función. TIENE QUE ESTAR SI O SI EN LA PRIMER LINEA.""" 
#     """Esta funcion devuelve la suma de los parametros a y b"""
#     return a + b
