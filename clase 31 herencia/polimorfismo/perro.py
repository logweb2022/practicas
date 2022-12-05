from animal import Animal

class Perro(Animal):
    def emitir_sonido(self):
        super().emitir_sonido()
        print("Guau")

    def mover(self):
        super().mover()

    def saluda(self):
        return super().saluda()
    

if __name__== '__main__':
    print("Valor de clase perro")
