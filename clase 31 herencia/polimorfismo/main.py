from perro import Perro
from gato import gato

def __main__():
    perro1 = Perro()
    perro1.emitir_sonido()
    perro1.mover()
    perro1.saluda()

    gato1 = gato()
    gato1.emitir_sonido()
    gato1.mover()
    gato1.saluda()

#Programa principal
if __name__== '__main__':
    __main__()#ejecutamos funcion main