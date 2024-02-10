#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""en mode console
demande les instructions et trace le systeme demandé
"""

import domaine.generateur as g

def demander_nombre_positif(message: str)-> int:
    """forcer l'utilisateur à rentrer un nombre positif.
    L'input de l'utilisateur est personnalisé par message.
    """
    while True:
        try:
            valeur: str = input(message)
            entier =  int(valeur)
            if entier >= 0:
                return entier
            else:
                print("Veuillez entrer un nombre entier positif")
        except ValueError:
            print("Veuillez entrer un nombre entier positif")


def demander_unite() -> int:
    unite : int = demander_nombre_positif('taille du segment')
    return unite

def demander_nombre_cycle() -> int:
    nb_cycle :int = demander_nombre_positif('nombre de cycle')
    return nb_cycle

def demander_quel_dessin() -> int:
    type_dessin : int = demander_nombre_positif("1 - uniquement dernière génération \n2 - cumuler les dessins")
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

#a = demander_nombre_positif('azert')
#print(type(a))