#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import interface.console_commande as cc

def initialiser_plante_wp_en_l_systeme() -> dict:
    alphabet : list[str] = ['F', 'X']
    variables : list = ['+', '-', '[', ']']
    axiome : str = "X"
    regles : dict = {"X" : "F+[[X]-X]-F[-FX]+X", "F" : "FF"}
    angle : float = float(25)
    facteur_division = 1
    systeme : dict = {'alphabet' : alphabet, 'variables' : variables,
               'axiome' : axiome, 'regles' : regles, 
               'angle' : angle, 'facteur_division' : facteur_division}
    return systeme

if __name__ == '__main__':    

    systeme = initialiser_plante_wp_en_l_systeme()
    cc.dessiner_choix(systeme)
