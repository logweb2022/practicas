#CADENA DE CARACTERES-------------------------------------------------------------------------------
# cadena = "Hola comision 22536!"
# print(type(cadena)) #type: imprime tipo de caracter. imprime str (tipo string)
# print(cadena[2]) #[2] imprime la segunda letra (siempre empezando desde 0)
# print(len(cadena)) #len imprime longitud
# print(cadena[-1]) #imprime primer caracter de atrás para adelante

##buscar
# print(cadena.find("Hola"))#imprime en qué posición encuentra la palabra "Hola"

#iteración
# for valor in cadena: #valor puede ser reemplazado por cualquier letra o palabra
#     print(valor)

# for valor in cadena:
#     if not valor.isnumeric(): #al tener el not imprime todos los valores no numericos. si le sacamos el not nos imprime solo los numericos
#         print(valor)

# for valor in cadena:
#     if not valor.isalnum(): #al tener el not imprime valores que no sean alfanumericos (letras y numeros)
#         print(valor)

# cadena = cadena.replace("hola", "Bienvenidos")#reemplazo uno por otro
# print(cadena.lower())#imprime en minuscula
# print(cadena.upper())#imprime en mayuscula
# print(cadena.capitalize())#imprime en mayuscula la primera letra de la oración

#replicar una cadena
# x = "123"
# print(x*10)

# x = 1
# y = 2
# print(x > y)#imprime comparación

#concatenar
# nombre = input("Ingrese su nombre: ")
# saludo="Hola "+ nombre
# print(saludo)

# print(cadena[5:13])#imprime los caracteres que estan desde la posicion 5 a la 13

# print(max(cadena))#imprime el elemento mas grande segun codigo ASCII
# print(min(cadena))#imprime el elemento mas chico segun codigo ASCII

# print('-'.join(cadena))#agrega entre letras el caracter solicitado entre comillas simples''
#print(cadena.split(' '))#corta lo solicitado entre comillas simples. en este caso los espacios

#f-strings: todos los nombres de las variables se reemplazan por sus respectivos valores
# legajo = 1222
# nombre = "maria"
# nota = 10
# print(f"legajo: {legajo} Nombre: {nombre} nota: {nota}")

#LISTAS---------------------------------------------------------------------------------------
# numeros = [1,7,3,6,5]
# palabras = ["Hola", "Casa", "Moto"]
# lista_vacia = []

#iterar
# for valor in palabras:
#     if valor == "Hola": #imprime solamente si esta la palabra hola
#         print(valor)

# print(len(numeros))
# print(palabras[2])#imprime palabra en esa posicion

# for i in range (len(numeros)): #para multiplicar por 2 los valores
#     numeros[i] = numeros[i]*2
#     print(numeros)

# palabras.append("Miercoles")#agrega al final miercoles
# palabras.insert(3, "Martes")#lo inserta en la posicion 3
# print(palabras)

# palabras.pop() #elimina la ultima posicion, a menos que le indiquemos la posicion entre ()
# palabras.remove("Casa")
# print(palabras)

# numeros.sort()#ordena la lista
# numeros.sort(reverse=True)#imprime la lista al reves

#print(sum(numeros))#suma elementos de la lista

#lista de listas (Matriz)
# matriz = [
#     [1,2],
#     [3,4],
#     [5,6]
# ]
# print(matriz)
# print(matriz[1])#imprime fila 1 [3,4] (arranca contando del 0 inclusive)
# print(matriz[2][1])#imprime fila 2 columna 1

#DICCIONARIOS------------------------------
# dicc = {"Ramiro": 39, "Luciano": 35, "Pedro": 20}
# print(dicc)
# print(dicc["Luciano"])#imprime el valor del solicitado

# for clave in dicc:
#     if dicc[clave] > 21:#imprime solo los que son mayores de 21
#         print(clave)
#         print(dicc[clave])#imprime el valor para cada clave

# for valor in dicc.values(): #imprime solo los valores
#     print(valor)

#TUPLA: conjunto de elementos separados por comas y encerrados entre paréntesis, como si fuesen una lista pero con funciones limitadas por ej no se pueden modificar.
# fecha = (14,11,2022, (12,5),(2,2))
# print(fecha)

# #desempaquetado
# dia,mes,año,fecha2,asistencia = fecha

# print(dia)
# print(mes)
# print(año)
# print(fecha2)
# print(asistencia)

# print("Elemento 2 de la tupla")
# print(fecha[2])

#conjunto
# conjunto = {-1,2,3,-2,25,10}
# print(conjunto)

#transformar lista a conjunto
lista = [20,30,45]
print(lista)
aConjunto = set(lista)
print(aConjunto)