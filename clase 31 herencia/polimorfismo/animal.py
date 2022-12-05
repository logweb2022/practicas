from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def mover(self):
        print("Avanza")

    @abstractclassmethod
    def emitir_sonido(self):
        print("Animal emite sonido", end="")#end concatena al final
    
    @abstractclassmethod #al ser abstracta despues hay que definirla en cada clase del tipo de animal
    def saluda(self):
        print("Da la pata")