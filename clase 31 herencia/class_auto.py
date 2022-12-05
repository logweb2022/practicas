from  class_Vehiculo import Vehiculo
class Auto(Vehiculo):
    def __init__(self, color, ruedas,motor):
        super().__init__(color, ruedas)#hace referencia al init de vehiculo #super() es igual a vehiculo(). es lo que hereda
        self.motor = motor#su propio atributo
    def __str__(self):
        return super().__str__() + "Tipo de motor: " + str(self.motor)

    def avanzar(self):
        super().avanzar()
        print ("El auto avanza")

#Programa principal
def __main__(): #creamos una funcion. puede estar como no estar. no cambia nada. aca lo usamos para que devuelva un print nada mas
    print("Soy parte del archivo de class_Auto")

if __name__== '__main__':
    __main__()