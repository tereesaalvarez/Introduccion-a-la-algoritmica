class media_notas:
    def __init__(self, nota1, nota2, nota3):
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
def media_aritmetica(self):
            return (self.nota1+self.nota2+self.nota3)/3
def media_ponderada(self, media_aritmetica):
        return round(media_aritmetica)

def introducir_nota(i):
   
    while True:
        nota=input("Introduce nota:")

        try:
            nota = float(nota)
            break
        except:
            print ("Cambia la coma por un punto")
            pass
    return nota


if __name__=="__main__":
    notas=[]
    for i in range(3):
        n= introducir_nota(i)
        notas.append(n)


total = media_aritmetica(notas[0], notas[1], notas[2])
print("La media aritmetia es: {}".format(total.media_aritmetica()))
print("La media ponderada es: {}".format(total.media_ponderada(total.media_aritmetica)))