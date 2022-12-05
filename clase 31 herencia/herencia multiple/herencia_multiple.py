class classic:
    def a(self):
        print("Tiene tarjeta bonificada")
class gold:
    def a(self):
        print("Suma millas")
    def b(self):
        print("Multiplica millas x 2")

class black(classic, gold):
    def __init__(self):
        print("Soy black")
    
    def c(self):
        print("Tengo seguro de vida bonificado")

#Programa principal
print("La clase classic")
classic1 = classic()
classic1.a()


print("Soy clase gold")
gold1 = gold()
gold1.a()
gold1.b()

print("Soy clase black")
black1= black()
black1.c()
black1.a()#imprimió el a de classic porque es el primer parametro que se ingresó
black1.b()

