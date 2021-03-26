# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 15:49:07 2021

@author: Lenovo
"""
from numpy import random

#parte 4
#Shows board with coordinates
def Create_Board(List):
    Board=[]
    i=0
    while i<len(List):
        r=0
        Sub_Board=[]
        while r<len(List[0]):
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
    String=str(input("Choose your coordinates: "))
    h=["(",")","."]
    for h in String:
        String=String.replace("(","")
        String=String.replace(")","")
        String=String.replace(".",",")
    Lista_Carta_Elegida=String.split(",")
    return(Lista_Carta_Elegida)


#parte 7 (Shows one chosen card in board)
def Show_Card_in_Board(List_Coordinates,List_Board,List_Values):
    x=int(List_Coordinates[0])#x coordinate
    y=int(List_Coordinates[1]) #y coordinate
    Value=List_Values[x][y]#valor al que corresponde la coordenada
    List_Board[x].pop(y)
    List_Board[x].insert(y,Value)
    return List_Board


#parte 9 (Shows 2 chosen cads in board)
def Show_Cards_in_Board(List_Coordinates1,List_Coordinates2,List_Board,List_Values):
    x1=int(List_Coordinates1[0])#x coordinate
    y1=int(List_Coordinates1[1]) #y coordinate
    Value1=List_Values[x1][y1]#valor al que corresponde la coordenada
    List_Board[x1].pop(y1)
    List_Board[x1].insert(y1,Value1)
    #####
    x2=int(List_Coordinates2[0])#x coordinate
    y2=int(List_Coordinates2[1]) #y coordinate
    Value2=List_Values[x2][y2]#valor al que corresponde la coordenada
    List_Board[x2].pop(y2)
    List_Board[x2].insert(y2,Value2)
    return List_Board

#prints boards
def Print_Board(List):
    i=0
    while i<len(List):
        print(List[i])
        i+=1 
        

def Delete_Cards_in_Board(List_Coordinates1,List_Coordinates2,List_Board,List_Values):
    x1=int(List_Coordinates1[0])#x coordinate
    y1=int(List_Coordinates1[1]) #y coordinate
    Value1=List_Values[x1][y1]#valor al que corresponde la coordenada
    List_Board[x1].pop(y1)
    List_Board[x1].insert(y1,"  ")
    #####
    x2=int(List_Coordinates2[0])#x coordinate
    y2=int(List_Coordinates2[1]) #y coordinate
    Value2=List_Values[x2][y2]#valor al que corresponde la coordenada
    List_Board[x2].pop(y2)
    List_Board[x2].insert(y2,"  ")
    return List_Board
 

def Compare_Cards(List_Coordinates1,List_Coordinates2,List_Board,Board):
    x1=int(List_Coordinates1[0])#x coordinate
    y1=int(List_Coordinates1[1]) #y coordinate
    x2=int(List_Coordinates2[0])#x coordinate
    y2=int(List_Coordinates2[1]) #y coordinate
    List_Board[x1].pop(y1)
    List_Board[x1].insert(y1,Board[x1][y1-1])
    List_Board[x2].pop(y2)
    List_Board[x2].insert(y2,Board[x2][y2-1]) 
    return List_Board


####################################################################
   
#parte 1
Number_of_Cards=int(input("Enter the number of cards you whant to play with: "))
List1=[]
List2=[]
i=0
r=1
while i<Number_of_Cards:
    List1.append(r)            #falta borrar los prints
    List2.append(r)
    r+=1
    i+=1


#parte 2                    
List1_Random=[]
List2_Random=[]
i=0
while i<Number_of_Cards:
    x=random.choice(List1)
    List1_Random.append(x)
    List1.remove(x)
    y=random.choice(List2)
    List2_Random.append(y)
    List2.remove(y)
    i+=1
Master_List=[]             #falta borrar los prints
Master_List.append(List1_Random)
Master_List.append(List2_Random)

#parte 3
Player1=0
Player2=0

##########################################
print("Player one starts ")
Coordinates_Board=Create_Board(Master_List)
v=0
Space_Counter=0

while Space_Counter<len(Master_List[0]):  
    Player1_Coordinates1=Input_Card_Coordinates()
    Print_Board(Show_Card_in_Board(Player1_Coordinates1,Coordinates_Board,Master_List))
    print("Player plays ##: ")
    Player1_Coordinates2=Input_Card_Coordinates()
    Print_Board(Show_Cards_in_Board(Player1_Coordinates1,Player1_Coordinates2,Coordinates_Board,Master_List))
    x1=int(Player1_Coordinates1[0])
    y1=int(Player1_Coordinates1[1])
    x2=int(Player1_Coordinates2[0])
    y2=int(Player1_Coordinates2[1])
    if Master_List[x1][y1]==Master_List[x2][y2]:
        print("Player one has found a pair ")
        Player1+=1  
        Space_Counter+=1
        if Space_Counter==len(Master_List):
            break
        else: 
            Print_Board(Delete_Cards_in_Board(Player1_Coordinates1,Player1_Coordinates2,Coordinates_Board,Master_List))
            print("Player one plays again ")
        continue
    else:
        print("Player one has missed ")
        Print_Board(Compare_Cards(Player1_Coordinates1,Player1_Coordinates2,Coordinates_Board,Coordinates_Board))
        print("Player 2 plays ")
    ####Player 2
    Player1_Coordinates2=Input_Card_Coordinates()
    Print_Board(Show_Cards_in_Board(Player1_Coordinates1,Player1_Coordinates2,Coordinates_Board,Master_List))
    x1=int(Player1_Coordinates1[0])
    y1=int(Player1_Coordinates1[1])
    x2=int(Player1_Coordinates2[0])
    y2=int(Player1_Coordinates2[1])
    if Master_List[x1][y1]==Master_List[x2][y2]:
        print("Player two has found a pair ")
        Player2+=1  
        Space_Counter+=1
        if Space_Counter==len(Master_List[0]):
            break
        else: 
            Print_Board(Delete_Cards_in_Board(Player1_Coordinates1,Player1_Coordinates2,Coordinates_Board,Master_List))
            print("Player two plays again ")
        continue
    else:
        print("Player two has missed ")
        Print_Board(Compare_Cards(Player1_Coordinates1,Player1_Coordinates2,Coordinates_Board,Coordinates_Board)) 
    
if Player1<Player2:
    print("Player 2 has won ")
else:
    print("Player 1 has won ")
