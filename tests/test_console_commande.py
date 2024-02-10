#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 18:02:14 2024

@author: silanoc
"""

import interface.console_commande as icc
#import mocker

def test_demander_unite(mocker):
    mocker.patch('input', return_value=100)
    reponse = icc.demander_unite()
    
    assert type(reponse) == int()
    
