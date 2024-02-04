from turtle import *
setup(width=1000,height=1000)
import tkinter as tk

"""
    F : Se déplacer d’un pas unitaire (∈ V)
    + : Tourner à gauche d’angle α (∈ S)
    - : Tourner à droite d’un angle α (∈ S)
    & : Pivoter vers le bas d’un angle α (∈ S)
    ^ : Pivoter vers le haut d’un angle α (∈ S)
    < : Roulez vers la gauche d’un angle α (∈ S)
    > : Roulez vers la droite d’un angle α (∈ S)
    | : Tourner sur soi-même de 180 ° (∈ S)
    [ : Sauvegarder la position courante (∈ S)
    ] : Restaurer la dernière position sauvée (∈ S)

Un L-système est une grammaire formelle qui comprend :

    Un alphabet V : l'ensemble des variables du L-système. V^* est l'ensemble des « mots » que l'on peut construire avec les symboles de V, et V^+ l'ensemble des mots contenant au moins un symbole.
    Un ensemble de valeur constantes S. Certains de ces symboles sont communs à tous les L-système (voir plus bas la Turtle interpretation).
    Un axiome de départ \omega choisi parmi V^+, c'est-à-dire l'état initial.
    Un ensemble de règles, noté P, de reproduction des symboles de V.

Un L-système est noté \{V, S, \omega, P\}.


Plante
{
angle 20
axiom X
X=F[+X]F[−X]+X
F=FF
}

"""

regle="X"
regleintermediaire=""
generation=0
unite=0
angle=20
Xencours=[]
Yencours=[]
Orientationencours=[]

def dessine():
    for i in range(len(regle)):
        if regle[i]=="F":
            forward(unite)
        elif regle[i]=="+":
            left(angle)
        elif regle[i]=="-":
            right(angle)
        elif regle[i]=="[":
            Xencours.append(xcor())
            Yencours.append(ycor())
            Orientationencours.append(heading())
        elif regle[i]=="]":
            penup()
            goto(Xencours[len(Xencours)-1],Yencours[len(Yencours)-1])
            setheading(Orientationencours[len(Orientationencours)-1])
            Xencours.pop()
            Yencours.pop()
            Orientationencours.pop()           
            pendown()

def generationsuivante(regleaconvertir):
    regleintermediaire=""
    for i in range(len(regleaconvertir)):
        if regleaconvertir[i]=="X":
            regleintermediaire=regleintermediaire+"F[+X]F[−X]+X"
        elif regleaconvertir[i]=="F":
            regleintermediaire=regleintermediaire+"FF"
        else:
            regleintermediaire=regleintermediaire+regle[i]
    return(regleintermediaire)
    
print(regle)
#dessine()
regle=generationsuivante(regle)
print(regle)
#dessine()
regle=generationsuivante(regle)
print(regle)
#dessine()
regle=generationsuivante(regle)
print(regle)
dessine()
regle=generationsuivante(regle)
print(regle)
#dessine()
regle=generationsuivante(regle)
print(regle)
#dessine()
regle=generationsuivante(regle)
dessine()





