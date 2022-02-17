class media_notas:
    def __init__(self, nota1, nota2, nota3):
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
    def media_aritmetica(self):
            return (self.nota1+self.nota2+self.nota3)/3
    def media_ponderada(self, media_aritmetica):
        return round(media_aritmetica)

def introducir_nota():
   
    while true:
        nota=input("Introduce nota:")

        try:
            nota = float(nota)
            break
        except:
            print ("Cambia la coma por un punto")
            pass
    return nota





if __name__=="__main__"