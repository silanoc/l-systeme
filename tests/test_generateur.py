#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour vérifier avec pytest que le script fonctionne.
- test_reecrire : facile
- test_dessiner_courbe : comparaison de fichier image. Explication dans 
le fichier methodologie_test.md
"""

import domaine.generateur as generateur
from PIL import Image
import turtle as t

def test_reecrire() -> None:
    """teste la fonction reecrire"""
    retour = generateur.reecrire('F', {'F':'F+F-F-F+F'})
    assert retour == 'F+F-F-F+F'
    
def test_dessiner_courbe() -> None:
    """test la fonction dessiner sur la première génération d'une coubre
    décrite par F+F-F-F+F et la compare à une image de référence.
    La comparaisons des images, se fait par la comparaison pixel par pixel de
    chaque image. Ils sont dans des listes via la fonction list(image.getdata())
    """
    
    #ouvrir l'image de référence et en récupérer les valeurs des pixels.
    image_reference = Image.open('./tests/test_courbe_arche.png')
    reference = list(image_reference.getdata())
    
    #fabriquer l'image et en récupérer les valeurs des pixels
    generateur.dessine('F+F-F-F+F', 50, 90)
    t.setup(500, 500)
    image = t.getcanvas()
    image.postscript(file="./tests/fabrique.png", colormode='color')
    image_fabrique = Image.open("./tests/fabrique.png")
    fabrique = list(image_fabrique.getdata())
    t.reset()
    t.bye()
    
    assert fabrique == reference
  
"""                             
def test_dessiner_arbre():
    #ouvrir l'image de référence et en récupérer les valeurs des pixels.
    image_reference = Image.open('./tests/test_arbre_de_base.png')
    reference = list(image_reference.getdata())
    
    #fabriquer l'image et en récupérer les valeurs des pixels
    generateur.dessine("F[-F][+F]", 50, 20)
    t.setup(500, 500)
    image = t.getcanvas()
    image.postscript(file="fabrique.png", colormode='color')
    image_fabrique = Image.open("fabrique.png")
    fabrique = list(image_fabrique.getdata())
    t.reset()
    t.bye()
    
    assert fabrique == reference
"""