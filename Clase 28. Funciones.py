#INTRUCCIONES DE LAS FUNCIONES-----------------------------
# def saludar(): #def palabra reservada que define una función
#     #intrucciones
#     print("Hola a todos")

# def saludar_con_nombre(nombre): 
#     print("Hola " + nombre)

# def sumar():
#     a = 10
#     b = 15
#     sumar = a + b
#     return sumar

# def sumar_con_parametros(a,b):
#     return a + b

# #devolver 2 parametros
# def parametros2(a, b):
#     sumar2 = a + b 
#     restar = a - b
#     return sumar2, restar

# def imprimir_mensaje_cinco_veces():
#     for i in range(5):
#         print("Este es el mensaje " + str(i))

# #por valor: se crea una copia local de la variable dentro de la funcion, no lo afecta por fuera. Se usa para los tipos simples: enteros, flotantes, cadenas, lógicos.
# def doblar_valor(numero):
#         numero*=2
#         print(numero)
# n =  10
# doblar_valor(n)
# print(n)

# #por referencia: se maneja directamente la variable, los cambios realizados dentro de la funcion le afectaran también afuera. se usa para tipos compuestos: listas, diccionarios, conjuntos.
# def doblar_valores(numeros):
#     for i, n in enumerate(numeros):
#         numeros[i] *=2

# ns = [10,50,100]        
# doblar_valores(ns)
# print(ns)

#def nombre (requeridos, opcionales) primero van los requeridos y dsp los opcionales
def sumar_con_parametros2(a, b = 90):#parametros opcionales. si no defino b queda como 90. si lo defino lo reemplaza
    sumar2 = a + b
    return sumar2

resultado2 = sumar_con_parametros2(25, 50)
print(resultado2)








#LLAMADO A LAS FUNCIONES------------------------------
# saludar()
# saludar_con_nombre("Jorge")
# resultado = sumar()
# print(resultado)

# resultado2 = sumar_con_parametros(25 , 50)
# print(resultado2)

# suma, resta = parametros2(15,10)
# print(suma)
# print(resta)
# imprimir_mensaje_cinco_veces()
# mensaje = imprimir_mensaje_cinco_veces()
# print(mensaje)

