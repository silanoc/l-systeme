#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import generateur as g

"""
Un L-système est noté \{V, S, \omega, P\}.
Plante
{
angle 20
axiom X
X=F[+X]F[−X]+X
F=FF
}
"""

#fr
# Initialiser
#variables: list = ['F', '+', '-']
axiome : str = "X"
regle : dict = {"X" : "F[+X]F[-X]+X", "F" : "FF"}
unite : str = 10
angle : str = 20 

"""
#GB
# Initialiser
#variables: list = ['F', '+', '-']
axiome : str = "X"
regle : dict = {"X" : "F+[[X]-X]-F[-FX]+X", "F" : "FF"}
unite : str = 10
angle : str = 25 
"""

# Calculer les ré-éctitures souhaitées
for i in range(5):
    axiome = g.reecrire(axiome, regle)
    print(axiome)

g.dessine(axiome, unite, angle)