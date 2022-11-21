class alumnos:
    def __init__(self, nombre, nota):
        self.nombre = input("Ingrese su nombre ")
        self.nota = int(input("Ingrese su nota "))

    def __str__(self):
        return(f'{self.nombre} obtuvo {self.nota} puntos')

    

    def mostrar_estado(self):
        print(f'El Estado de {self.nombre} es {self.nota}')
        if self.nota<4:
            print("Desaprobó")
        elif self.nota<9:
            print("Bueno")
        else:
            print("Excelente")


alumno1 = alumnos("Nacho", 10)
print(alumno1)
alumno1.mostrar_estado()

