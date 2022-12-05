from animal import Animal

class gato(Animal):
    def emitir_sonido(self):
        super().emitir_sonido()
        print("Miau")

    def mover(self):
        super().mover()
    
    def saluda(self):
        print("No doy la pata")

if __name__== '__main__':
    print("Valor de clase gato")
