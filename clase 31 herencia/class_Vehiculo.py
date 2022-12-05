"""Herencia simple

"""
class Vehiculo():#clase padre/ super clase
    def __init__(self, color, ruedas):
        self.color = color #un atributo
        self.ruedas = ruedas#otro atributo
    
    def __str__(self):#un metodo
        return f'Color: {self.color}, Cantidad de ruedas: {self.ruedas}' 

    def avanzar(self):#otro metodo
       pass


