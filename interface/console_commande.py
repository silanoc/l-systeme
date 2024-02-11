#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Toutes les commandes pour l'affichage en mode console.
demande les instructions et trace le systeme demandé
"""

import os, sys
import domaine.generateur as g
# importer les fichiers du bestiaire
import bestiaire.arbre_de_base
import bestiaire.courbe_de_Koch_triangle
import bestiaire.courbe_quadratique_de_Koch_type_1
import bestiaire.courbe_quadratique_de_Koch_type_2
import bestiaire.flocon_de_Koch
import bestiaire.plante_1
import bestiaire.plante_2


###
# Parametrage des dessins
###

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
    type_dessin :int = demander_quel_dessin()
    print(type_dessin)
    unite : int = demander_unite()
    nb_tour : int = demander_nombre_cycle()
    if type_dessin == 1 :
        g.reecrire_puis_dessine(systeme['axiome'], systeme['regles'], unite, systeme['angle'], nb_tour)
    elif type_dessin == 2 :
        g.reecrire_cumul_dessin(systeme['axiome'], systeme['regles'], unite, systeme['angle'], nb_tour, systeme['facteur_division'])

###
# fonctions diverses
###

def appuyer_pour_la_suite() -> None:
    input("appuyer sur n'importe quel touche pour la suite")
    
def demander_choix_courbe() -> int:
    choix_courbe : int = demander_nombre_positif("votre_choix")
    return choix_courbe

def lancer_courbe_choisie(choix : int) -> None:
    dict_bestiaire : dict = {1 : bestiaire.arbre_de_base.initialiser_arbre_de_base,
                      2 : bestiaire.courbe_de_Koch_triangle.initialiser_courbe_koch_triangle,
                      3 : bestiaire.courbe_quadratique_de_Koch_type_1.initialiser_courbe_koch_carre,
                      4 : bestiaire.courbe_quadratique_de_Koch_type_2.initialiser_courbe_koch_carre_type_2,
                      5 : bestiaire.flocon_de_Koch.initialiser_flocon_koch,
                      6 : bestiaire.plante_1.initialiser_plante_wp_fr_l_systeme,
                      7 : bestiaire.plante_2.initialiser_plante_wp_en_l_systeme}
    dessiner_choix(dict_bestiaire[choix]())
    
def efface_console() -> None:
    """Pour nettoyer la console entre chaque vue, et avoir quelque chose de propre."""
    if sys.platform.startswith("win"): #si windows
        os.system("cls")
    else:
        os.system("clear")

def fin() -> None:
    """Message quand on quitte le programme"""
    efface_console()
    print("Merci d'avoir utilisé mon programme. A une prochaine fois.")
    exit()
        