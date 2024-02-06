#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle as t

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
    Règle : (F → F+F-F-F+F)

"""

###
# fonctions de base
###

def reecrire(axiome_a_convertir : str, regle : dict ) -> str :
    """changer les axiome d'une fois à l'autre en fonction des regles de réécritre"""
    axiome_intermediaire : str = ""
    variables_a_transformer = regle.keys()
    for i in range(len(axiome_a_convertir)):
        if axiome_a_convertir[i] in variables_a_transformer:
            axiome_intermediaire = axiome_intermediaire + regle[axiome_a_convertir[i]]
        else:
            axiome_intermediaire = axiome_intermediaire + axiome_a_convertir[i]
    return axiome_intermediaire

def dessine(axiome_a_appliquer : str, unite_dessin : int, angle_dessin) -> None:
    """avec tutrle dessine l'axiome en entrée"""
    position_courant :list = []
    orientation_courant : list = []
    for i in range(len(axiome_a_appliquer)):
        if axiome_a_appliquer[i] == "F":
            t.forward(unite_dessin)
        elif axiome_a_appliquer[i] == "+":
            t.left(angle_dessin)
        elif axiome_a_appliquer[i] == "-":
            t.right(angle_dessin)
        elif axiome_a_appliquer[i] =="[":
            position_courant.append(t.position())
            orientation_courant.append(t.heading())
            print(t.pos(), t.heading())
        elif axiome_a_appliquer[i] =="]":
            t.penup()
            t.goto(position_courant[-1])
            t.setheading(orientation_courant[-1])
            position_courant.pop(-1)
            orientation_courant.pop(-1)
            t.pendown()
        elif axiome_a_appliquer[i] == "X":
            pass
    t.Screen()

###
# enchainements graphiques
###

def reecrire_puis_dessine(axiome :str, regle : dict, unite : int, angle : int, nb_tour : int):
    """fait plusieur ré-écriture et génére le tracé final"""
    for i in range(nb_tour):
        axiome = reecrire(axiome, regle)
        print(axiome)
    dessine(axiome, unite, angle)
    
def reecrire_cumul_dessin(axiome :str, regle : dict, unite : int, angle : int, nb_tour : int, facteur_division : int):
    """trace chaque réécriture de façon juxtaposé"""
    couleur = ['grey', 'black', 'red', 'green', 'blue' ]
    t.speed(10)
    for i in range(nb_tour):
        t.pencolor(couleur[i])
        print(axiome)
        dessine(axiome, unite, angle)
        axiome = reecrire(axiome, regle)
        unite = unite / facteur_division #attention division par zéro
        t.penup()
        t.home()
        t.pendown()

###
# fonction pour controler vi un exemple connu de wikipedia
###

def test_koch_1():
    variables: list = ['F', '+', '-']
    axiome : str = "F"
    regle : dict = {"F" : "F+F-F-F+F"}
    unite : int = 10
    angle : int = 90
    reecrire_puis_dessine(axiome, regle, unite, angle, 3)

def test_koch_2():
    variables: list = ['F', '+', '-']
    axiome : str = "F"
    regle : dict = {"F" : "F+F-F-F+F"}
    unite : int = 300
    angle : int = 90
    reecrire_cumul_dessin(axiome, regle, unite, angle, 5, 3)


if __name__ == '__main__':    
    
    test_koch_1()
    #test_koch_2()