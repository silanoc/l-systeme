#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:49:51 2024

@author: silanoc
"""

import generateur

def test_reecrire():
    retour = generateur.reecrire('F', {'F':'F+F-F-F+F'})
    assert retour == 'F+F-F-F+F'
                                       