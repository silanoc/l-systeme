#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle as t


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
image.postscript(file="test.png", colormode='color')
