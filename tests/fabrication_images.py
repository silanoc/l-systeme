#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle as t

def dessine_courbe_arche():

    t.setup(500, 500)
    
    taille = 50
    
    t.forward(taille)
    t.left(90)
    t.forward(taille)
    t.right(90)
    t.forward(taille)
    t.right(90)
    t.forward(taille)
    t.left(90)
    t.forward(taille)
    
    image = t.getcanvas()
    image.postscript(file="test_courbe_arche.png", colormode='color')
    
def dessine_arbre_de_base():
    
    t.setup(500, 500)
    
    taille = 50
    
    #t.setheading(90)
    t.forward(taille)
    t.left(20)
    t.forward(taille)
    t.forward(taille * -1)
    t.right(20 * 2)
    t.forward(taille)
    t.forward(taille * -1)
    
    image = t.getcanvas()
    image.postscript(file="test_arbre_de_base.png", colormode='color')
    
if __name__ == '__main__':   
    
    #dessine_courbe_arche()
    dessine_arbre_de_base()
    
    
    
    
    
