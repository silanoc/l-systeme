#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import interface.console_commande as cc

def message_debut() -> str:
    message :str = """
    +----------------------------------------------------------------------+
    |    Bienvenue dans ce petit logiciel de dessin de L-systeme en Turtle |
    +----------------------------------------------------------------------+
    """
    return message
    
def message_choisir_une_courbe() -> str:
    message : str = """Veuillez écrire le numéro de la courbe de votre choix : \n
    1 : arbre de base \n
    2 : courbe de Koch triangulaire \n
    3 : courbe_quadratique_de_Koch_type_1 \n
    4 : courbe_quadratique_de_Koch_type_2 \n
    5 : flocon_de_Koch\n
    6 : plante_1\n
    7 : plante_2
    """
    return message

def action_principale() -> None:
    """demander la courbe voulu, puis la parametrer puis la dessiner"""
    print(message_choisir_une_courbe())
    dessin_choisi = cc.demander_choix_courbe()
    cc.lancer_courbe_choisie(dessin_choisi)
    

def programme() -> None:
    """La partie qui est lancer pour tout le programme dans sa version console"""
    # Intro
    cc.efface_console()
    print(message_debut())
    cc.appuyer_pour_la_suite()
    # zone principale
    message : str = ""
    while message not in ['Q', 'q']:
        cc.efface_console()
        action_principale()
        # Continuer ou quitter
        message = input("""appuyer sur Q ou q pour arrêter,\nsur n'importe quelle touche pour refaire une courbe""")
        if message in ['Q', 'q']:
            cc.fin()
    
if __name__ == '__main__':   
    
    programme()