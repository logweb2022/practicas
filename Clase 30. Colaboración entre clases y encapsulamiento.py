#actividad banco
class Cliente:
    banco = "Nacion"#atributo de clase

    def __init__(self, nom):#constructor
        self.nombre = nom
        self.saldo = 0

    def depositar(self,importe):
        self.saldo += importe #es igual a self.saldo = self.saldo + importe
        #To-Do: importe > 0
    def extraer(self,importe):
        self.saldo -= importe #es igual a self.saldo = self.saldo - importe
        #To-Do: verificar que el saldo > importe y saldo >0
    
    #Getter: pedir informacion (solo hacemos una consulta). retorna un dato (aca el saldo)
    def obtener_saldo(self): #no se pone parametro porque no necesitamos ingresar nada, solo obtener dato
        return(self.saldo)
        #otra opcion: print(srt(self.saldo))
    def __str__(self):#imprimir para devolver datos del cliente
        cadena = "Nombre: " + self.nombre + " Saldo: " + str(self.saldo)
        return cadena

        #otra opcion: usando "f strings"
        #return (f'"Nombre:" {self.nombre} Saldo: {str(self.saldo)}')

class Banco:
    def __init__(self) -> None:
        self.cli1 = Cliente("Maria")
        self.cli2 = Cliente("Juan")
        self.cli3 = Cliente("Juana")

    def deposito(self):
        #importe = int(input("Cuánto queres depositar?"))
        self.cli1.depositar(12500)
        self.cli2.depositar(11500)
        self.cli3.depositar(15200)
        self.cli1.depositar(500)
        print("Se depositó de forma correcta")

    def extraccion(self):
        #importe = int(input("Cuánto queres depositar?"))
        self.cli2.extraer(7800)
        self.cli3.extraer(5200)

    def depositos_totales(self):
        total = self.cli1.obtener_saldo() + self.cli2.obtener_saldo() + self.cli3.obtener_saldo()
        print("Caja: $" + str(total))

    def __str__(self) -> str:
        cadena = str(self.cli1) + "\n" + str(self.cli2) + "\n" + str(self.cli3) #\n es salto de línea
        return cadena

    #Línea desde donde empezamos a ejecutar el código
if __name__ == '__main__':
    banco1 = Banco()#en banco1 se almacena el resultado de instanciar la clase Banco
    print(banco1)
    banco1.deposito()
    print(banco1)
    banco1.depositos_totales()
    banco1.extraccion()
    banco1.depositos_totales()
    print(banco1)#para ver como cambiaron los objetos