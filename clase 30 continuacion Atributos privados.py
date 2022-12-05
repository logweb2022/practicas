class Cliente:
    # """Ocultar información
    # "Público": se puede acceder y modificar
    # "_Protegidos" (Débilmente privado): significa que no se debería poder acceder desde afuera al atributo, pero si se puede hacer. Se declara al princio con _ (1 guión bajo)
    # "__Privados: Fuertemente privado): no vamos a poder acceder desde afuera al atributo. da error. Se declara al princio con __ (2 guión bajo)
    # """
    # _direccion_banco = "Calle flase 123"#Atributo débilmente privado
    # __banco = "Nacion" #atributo fuertemente privado

# if __name__ == '__main__':
#     print(Cliente._direccion_banco)#devuelve la info por ser débilmente privado. MALA PRACTICA
#     print(Cliente.__banco)#da error por ser fuertemente privado

    def __init__(self, nombre, apellido):
        self.nombre = nombre #atributo de instancia
        self.apellido = apellido #lo hacemos publico al no tener ningun _ por lo que vamos a poder acceder y modificarlo
        self.saldo = 0

    def depositar(self,importe):
        self.saldo += importe

    def extraer(self,importe):
        self.saldo -= importe
    

    def __str__(self):#mostramos info del objeto
        cadena = "Nombre: " + self.nombre + " Apellido: " + self.apellido + (" Saldo:$ ") + str(self.saldo)
        return cadena

#1ro se declaran los getters
#2do se declaran los setters
#getter para saldo
@property #decorador para getter
def saldo(self):
    return self.saldo

@property
def nombre(self):
    return self.nombre

@property
def apellido(self):
    return self.apellido

@nombre.setter
def nombre(self,nombre):
    self.nombre = nombre

@apellido.setter
def apellido(self, apellido):
    self.apellido = apellido

if __name__ == '__main__':
   # print(Cliente._direccion_banco)#devuelve la info por ser débilmente privado. MALA PRACTICA
#    print(Cliente.__banco)#da error por ser fuertemente privado
    cli1 = Cliente("Luciano", "Signorelli")
    print(cli1.nombre)#da error por ser privado (cuando el atributo tiene los __)
    cli1.depositar(1200)
    cli1.extraer(200)
    print(cli1.saldo)
    cli1.nombre = "Rodrigo" # para cambiar nombre al cliente
    print(cli1)
    
    