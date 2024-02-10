#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:11:37 2024

@author: silanoc

source https://accromath.uqam.ca/2013/09/l-systemes-les-equations-des-plantes/
"""
import domaine.generateur as g

# Initialiser
#variables: list = ['F', '+', '-']
axiome : str = "F"
regle : dict = {"F" : "F[-F][+F]"}
#regle : dict = {"F" : "S[-F][+F]"}
unite : int = 50
angle : int = 30 


# Calculer les ré-éctitures souhaitées
print(axiome)
g.dessine(axiome, unite, angle)
for i in range(2):
    axiome = g.reecrire(axiome, regle)
    print(axiome)
    g.dessine(axiome, unite, angle)


#g.dessine(axiome, unite, angle)


#g.reecrire_puis_dessine(axiome, regle, unite, angle, 2)
#g.reecrire_cumul_dessin(axiome, regle, unite, angle, 10, 1)