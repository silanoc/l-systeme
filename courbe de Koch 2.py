#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import generateur as g

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

"""

# Initialiser
variables: list = ['F', '+', '-']
axiome : str = "F"
regle : dict = {"F" : "F+F-F-FF+F+F-F"}
unite : int = 10
angle : int = 90
    
#g.reecrire_puis_dessine(axiome, regle, 10, angle, 3)
g.reecrire_cumul_dessin(axiome, regle, 500, angle, 5, 4)
