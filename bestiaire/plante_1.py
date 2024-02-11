#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import interface.console_commande as cc


"""
source : https://fr.wikipedia.org/wiki/L-Syst%C3%A8me#Exemple_d'un_D0L-syst%C3%A8me

Plante
{
angle 20
axiom X
X=F[+X]F[−X]+X
F=FF
}

ATTENTION : F autorise la tortue à se déplacer, pas X qui conte comme "rien"

"""

def initialiser_plante_wp_fr_l_systeme() -> dict:
    alphabet : list[str] = ['F', 'X']
    variables : list = ['+', '-', '[', ']']
    axiome : str = "X"
    regles : dict = {"F" : "FF", "X" : "F[+X]F[-X]+X"}
    angle : float = float(20)
    facteur_division = 1
    systeme : dict = {'alphabet' : alphabet, 'variables' : variables,
               'axiome' : axiome, 'regles' : regles, 
               'angle' : angle, 'facteur_division' : facteur_division}
    return systeme

if __name__ == '__main__':    

    systeme = initialiser_plante_wp_fr_l_systeme()
    cc.dessiner_choix(systeme)

























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
        else:
            pass

def generationsuivante(regleaconvertir):
    regleintermediaire=""
    for i in range(len(regleaconvertir)):
        if regleaconvertir[i]=="X":
            regleintermediaire=regleintermediaire+"F[+X]F[-X]+X"
        elif regleaconvertir[i]=="F":
            regleintermediaire=regleintermediaire+"FF"
        else:
            regleintermediaire=regleintermediaire+regle[i]
    return(regleintermediaire)
    
print(regle)
dessine()
regle=generationsuivante(regle)


print(regle)
dessine()

"""

"""
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
"""





