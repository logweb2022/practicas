#try-catch: capturar y manejar excepciones: de las más específicas a las más genéricas
#provocamos varios errores y le damos un título a cada uno
def ingresar_valor():
    num1 = int(input("Ingrese un numero: "))
    return num1
def dividir(n1,n2):
    return n1 /n2
#Prog Principal
if __name__ == '__main__':
    try:
        num1 = ingresar_valor()
        num2 = ingresar_valor()
        resultado = dividir(num1,num2)
    except ValueError:
        print("Ingrese un valor númerico")
    except ZeroDivisionError:
        print("El divisor no puede ser 0 (cero)")
    except:
        print("Ha ocurrido un error!")
    else: #Si no ocurre error
        print("El valor de la div es: ", resultado)