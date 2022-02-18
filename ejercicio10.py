class triangulo: 
    def __init__(self, alto, lado):
        self.alto= alto
        self.lado= lado
    def area(self):
        return(self.alto*self.lado)/2

def datos(dato):
    while True:
        numero= input("introduce numero {}".format(dato))
        try:
            numero = float(numero)
            break
        except:
            print("Introduzca un valor que sirva")
            pass
    return numero


if __name__ == "__main__":
    lado= datos("lado")
    alto= datos("altura")
    resultado= triangulo(alto,lado)
    print("el area del triangulo es {}".format(resultado.area()))
