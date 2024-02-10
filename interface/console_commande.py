#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""en mode console
demande les instructions et trace le systeme demandé
"""

import domaine.generateur as g

def demander_unite() -> int:
    unite : int = int(input('taille du segment'))
    return unite

def demander_nombre_cycle() -> int:
    nb_cycle :int = int(input('nombre de cycle'))
    return nb_cycle

def demander_quel_dessin() -> int:
    type_dessin : int = int(input("1 - uniquement dernière génération \n 2 - cumuler les dessins"))
    return type_dessin

def dessiner_choix(systeme)-> None:
    #systeme = systeme
    type_dessin = demander_quel_dessin()
    print(type_dessin)
    unite = demander_unite()
    nb_tour = demander_nombre_cycle()
    
    if type_dessin == 1 :
        g.reecrire_puis_dessine(systeme['axiome'], systeme['regles'], unite, systeme['angle'], nb_tour)
    elif type_dessin == 2 :
        g.reecrire_cumul_dessin(systeme['axiome'], systeme['regles'], unite, systeme['angle'], nb_tour, systeme['facteur_division'])
