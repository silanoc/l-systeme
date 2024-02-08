#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:45:10 2024

@author: silanoc
"""

import console_commande as cc

"""
Courbe de Koch triangle
- Variable : v = {F}
- Constantes : S = {+, −}
- Axiome : w = F
- Règle : (F → F+F-F+F)
"""

def initialiser_courbe_koch_triangle() -> dict:
    alphabet : list = ['F']
    variables : list = ['+', '-']
    axiome : str = "F"
    regles : dict = {"F" : "F+F--F+F"}
    angle : float = float(60)
    facteur_division = 3
    systeme : dict = {'alphabet' : alphabet, 'variables' : variables,
               'axiome' : axiome, 'regles' : regles, 
               'angle' : angle, 'facteur_division' : facteur_division}
    return systeme
 

if __name__ == '__main__':    

    systeme = initialiser_courbe_koch_triangle()
    cc.dessiner_choix(systeme)