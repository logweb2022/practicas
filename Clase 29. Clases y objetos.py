#Declarar clase: se hace con la palabra reservada class
class persona:
    piernas = 2 #este es un atributo de clase. son las caracteristicas de la clase (grupo) que se comparten
    brazos = 2
    #Características de cada uno
    def inicializar(self,nombre,edad): #siempre se usa self como primer parametro y haciendo referencia a la clase
        self.nombre = nombre 
        self.edad = edad

    def imprimir(self):
        print("Nombre: " + self.nombre + " Edad: " + str(self.edad)) #str: cuando lo imprime lo pasa a string

    def saludar(self,nombre):
        print("Hola " + nombre)

#Programa principal
persona1 = persona() #ESTO ES INSTANCIAR. Instanciamos un objeto de la clase persona
persona1.inicializar("Nacho", 31)#ingresamos atributos
persona1.imprimir()
persona1.saludar("Juan")
print(persona1.piernas)#imprime atributo piernas
persona.piernas= 3 #podemos cambiar el atributo----
persona2 = persona() #ESTO ES INSTANCIAR
persona2.inicializar("Pedro", 40)
persona2.imprimir()


print(persona2.piernas)