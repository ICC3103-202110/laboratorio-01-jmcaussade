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
print("Lista Maestra ",Lista_Maestra)


    

