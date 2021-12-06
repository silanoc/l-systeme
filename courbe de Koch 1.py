from turtle import *
setup(width=1000,height=500)
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


    Variable : v = {F}
    Constantes : S = {+, −}
    Axiome : w = F
    Règle : (F → F+F−F−F+F)


"""

regle="F"
regleintermediaire=""
generation=0
unite=10

def dessine():
    for i in range(len(regle)):
        if regle[i]=="F":
            forward(unite)
        if regle[i]=="+":
            left(90)
        if regle[i]=="-":
            right(90)

def generationsuivante(regleaconvertir):
    regleintermediaire=""
    for i in range(len(regleaconvertir)):
        if regleaconvertir[i]=="F":
            regleintermediaire=regleintermediaire+"F+F-F-F+F"
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
#dessine()
regle=generationsuivante(regle)
print(regle)
dessine()
regle=generationsuivante(regle)





