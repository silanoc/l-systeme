#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle as t
from typing import Union
FloatInt = Union[float, int] #typage float ou int

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

def dessine(axiome_a_appliquer : str, unite_dessin : FloatInt, angle_dessin) -> None:
    """avec tutrle dessine l'axiome en entrée
    seul F fait avancer la tortue"""
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
        else:
            pass
    t.Screen()

###
# enchainements graphiques
###

def reecrire_puis_dessine(axiome :str, regle : dict, unite : int, angle : int, nb_tour : int) -> None:
    """fait plusieur ré-écriture et génére le tracé final"""
    for i in range(nb_tour):
        axiome = reecrire(axiome, regle)
        print(axiome)
    dessine(axiome, unite, angle)
    
def reecrire_cumul_dessin(axiome :str, regle : dict, unite : FloatInt, angle : int, nb_tour : int, facteur_division : int = 1) -> None:
    """trace chaque réécriture de façon juxtaposé"""
    couleur = ['grey', 'black', 'red', 'green', 'blue' ]
    t.speed(10)
    for i in range(nb_tour):
        t.pencolor(couleur[i])
        print(axiome)
        dessine(axiome, unite, angle)
        axiome = reecrire(axiome, regle)
        try:
            unite = unite / facteur_division 
        except ZeroDivisionError:
            print("Attention, le facteur de division vaut Zéro et génére donc une erreur de divison. Le programme est arrêté")
            break
        t.penup()
        t.home()
        t.pendown()

###
# fonction pour controler via un exemple connu de wikipedia
###

def test_koch_1() -> None:
    alphabet : list = ["F"]
    variables: list = ['+', '-']
    axiome : str = "F"
    regle : dict = {"F" : "F+F-F-F+F"}
    unite : int = 10
    angle : int = 90
    reecrire_puis_dessine(axiome, regle, unite, angle, 3)

def test_koch_2() -> None:
    alphabet : list[str] = ["F"]
    variables: list = ['+', '-']
    axiome : str = "F"
    regle : dict = {"F" : "F+F-F-F+F"}
    unite : int = 300
    angle : int = 90
    reecrire_cumul_dessin(axiome, regle, unite, angle, 5, 3)


if __name__ == '__main__':    
    
    #test_koch_1()
    test_koch_2()