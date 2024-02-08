#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import console_commande as cc

"""
Flocon de Koch 
- Variable : v = {F}
- Constantes : S = {+, −}
- Axiome : w = F--F--F
- Règle : (F → F+F-F+F)
"""

def initialiser_flocon_koch() -> dict:
    alphabet : list = ['F']
    variables : list = ['+', '-']
    axiome : str = "F--F--F"
    regles : dict = {"F" : "F+F--F+F"}
    angle : float = float(60)
    facteur_division = 3
    systeme : dict = {'alphabet' : alphabet, 'variables' : variables,
               'axiome' : axiome, 'regles' : regles, 
               'angle' : angle, 'facteur_division' : facteur_division}
    return systeme
 

if __name__ == '__main__':    

    systeme = initialiser_flocon_koch()
    cc.dessiner_choix(systeme)