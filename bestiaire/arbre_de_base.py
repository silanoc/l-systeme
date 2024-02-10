#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import interface.console_commande as cc

"""
source https://accromath.uqam.ca/2013/09/l-systemes-les-equations-des-plantes/

- Variable : v = {F, S}
- Constantes : S = {+, −}
- Axiome : w = F
- Règle : (F → F[-F][+F]) ou - Règle : (F → S[-F][+F])
"""

def initialiser_arbre_de_base() -> dict:
    alphabet : list[str] = ['F']
    variables : list = ['+', '-']
    axiome : str = "F"
    regles : dict = {"F" : "F[-F][+F]"}
    angle : float = float(30)
    facteur_division = 1
    systeme : dict = {'alphabet' : alphabet, 'variables' : variables,
               'axiome' : axiome, 'regles' : regles, 
               'angle' : angle, 'facteur_division' : facteur_division}
    return systeme
 

if __name__ == '__main__':    

    systeme = initialiser_arbre_de_base()
    cc.dessiner_choix(systeme)