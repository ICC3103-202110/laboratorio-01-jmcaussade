from numpy import random
#parte 1
Numero_Cartas=int(input("Ingresa el número de cartas: "))
Lista1=[]
Lista2=[]
i=0
r=1
while i<Numero_Cartas:
    Lista1.append(r)            #falta borrar los prints
    Lista2.append(r)
    r+=1
    i+=1
print(Numero_Cartas)
print(Lista1)
print(Lista2)
print("#####")

#parte 2                    
Lista1_Random=[]
Lista2_Random=[]
i=0
while i<Numero_Cartas:
    x=random.choice(Lista1)
    Lista1_Random.append(x)
    Lista1.remove(x)
    y=random.choice(Lista2)
    Lista2_Random.append(y)
    Lista2.remove(y)
    i+=1
Lista_Maestra=[]             #falta borrar los prints
Lista_Maestra.append(Lista1_Random)
Lista_Maestra.append(Lista2_Random)
print("Lista 1 ",Lista1)                
print("Lista1_Random ", Lista1_Random)
print("Lista 2 ",Lista2)
print("Lista2_Random ", Lista2_Random)
print("Lista Maestra ",Lista_Maestra)#lista con valores de las cartas

#parte 3
Jugador1=0
Jugador2=0

#parte 4
#Shows board with coordinates
def Creat_Board():
    Board=[]
    i=0
    while i<len(Lista_Maestra):
        r=0
        Sub_Board=[]
        while r<len(Lista_Maestra[0]):
            Coordinates=[]
            Coordinates.append(i)
            Coordinates.append(r)
            Sub_Board.append(Coordinates)
            r+=1
        Board.append(Sub_Board)
        print(Sub_Board)
        i+=1
    return Board #returns straight board

#parte 5 (Asks for the card coordinates)
def Input_Card_Coordinates():
    String=str(input("Ingresa las coordenadas te tu carta: "))
    print(String)
    h=["(",")","."]
    for h in String:
        String=String.replace("(","")
        String=String.replace(")","")
        String=String.replace(".",",")
    print(String)
    Lista_Carta_Elegida=String.split(",")
    print(Lista_Carta_Elegida)
    return(Lista_Carta_Elegida)
#hay que revisar de aqui en adelante
#print(Input_Card_Coordinates())
#print("ahora viene tablero coordenadas")
#print(Creat_Board())
def Show_Cards_in_Board(List_Coordinates,List_Board,List_Values):
    x=int(List_Coordinates[0])#x coordinate
    print("valor x",x)
    y=int(List_Coordinates[1]) #y coordinate
    print("valor y",y)
    Value=List_Values[x][y]#valor al que corresponde la coordenada
    print("value",Value,"\n") #hasta qui bien
    List_Board[x].pop(y)
    List_Board[x].insert(y,Value)
    return List_Board

print(Show_Cards_in_Board(Input_Card_Coordinates(),Creat_Board(),Lista_Maestra))
    




    

