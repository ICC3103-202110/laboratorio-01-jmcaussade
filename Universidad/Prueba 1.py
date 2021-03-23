print("Hello world")
def Matriz(Alto,Ancho):
    Alto=int(Alto)
    Ancho=int(Ancho)
    i=0
    Lista=[]
    while i<Alto:
        r=0
        Sublista=[]
        while r<Ancho:
            Sublista.append(1)
            r+=1
        Lista.append(Sublista)
        i+=1
        print(Sublista)
print(Matriz(4,4))