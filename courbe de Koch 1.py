#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import generateur as g

"""
Un L-système est noté \{V, S, \omega, P\}.
    Variable : v = {F}
    Constantes : S = {+, −}
    Axiome : w = F
    Règle : (F → F+F-F-F+F)
"""

# Initialiser
variables: list = ['F', '+', '-']
axiome : str = "F"
regle : dict = {"F" : "F+F-F-F+F"}
unite :str = 10
angle :str = 90

#g.reecrire_puis_dessine(axiome, regle, 10, angle, 3)
g.reecrire_cumul_dessin(axiome, regle, 500, angle, 5, 3)
