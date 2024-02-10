#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import interface.console_commande as cc

"""
Courbe de Koch carrée
- Variable : v = {F}
- Constantes : S = {+, −}
- Axiome : w = F
- Règle : (F → F+F-F-F+F)
"""

def initialiser_courbe_koch_carre() -> dict:
    alphabet : list = ['F']
    variables : list = ['+', '-']
    axiome : str = "F"
    regles : dict = {"F" : "F+F-F-F+F"}
    angle : float = float(90)
    facteur_division = 3
    systeme : dict = {'alphabet' : alphabet, 'variables' : variables,
               'axiome' : axiome, 'regles' : regles, 
               'angle' : angle, 'facteur_division' : facteur_division}
    return systeme
 

if __name__ == '__main__':    

    systeme = initialiser_courbe_koch_carre()
    cc.dessiner_choix(systeme)