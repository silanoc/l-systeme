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

def dessine(axiome_a_appliquer : str, unite_dessin : int, angle_dessin) -> None:
    """avec tutrle dessine l'axiome en entrée"""
    for i in range(len(axiome_a_appliquer)):
        if axiome_a_appliquer[i] == "F":
            t.forward(unite_dessin)
        elif axiome_a_appliquer[i] == "+":
            t.left(angle_dessin)
        elif axiome_a_appliquer[i] == "-":
            t.right(angle_dessin)
    t.Screen()

def reecrire(axiome_a_convertir, regle):
    axiome_intermediaire = ""
    variables_a_transformer = regle.keys()
    for i in range(len(axiome_a_convertir)):
        if axiome_a_convertir[i] in variables_a_transformer:
            axiome_intermediaire = axiome_intermediaire + regle[axiome_a_convertir[i]]
        else:
            axiome_intermediaire = axiome_intermediaire + axiome_a_convertir[i]
    return(axiome_intermediaire)

def test_koch():
    variables: list = ['F', '+', '-']
    axiome : str = "F"
    regle : dict = {"F" : "F+F-F-F+F"}
    unite :str = 10
    angle :str = 90
    
    for i in range(3):
        axiome = reecrire(axiome, regle)
        print(axiome)
        dessine(axiome, unite, angle)
        
    

if __name__ == '__main__':    
    
    test_koch()