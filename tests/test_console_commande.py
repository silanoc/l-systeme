#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import interface.console_commande as icc

"""
utilisation de     
monkeypatch.setattr('builtins.input', lambda _: '42')
pour simuler un input dans le test
"""


def test_demander_nombre_positif(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '42')
    reponse = icc.demander_nombre_positif('un nombre')
    assert isinstance(reponse, int) and reponse >= 0
    
def test_demander_unite(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '42')
    reponse = icc.demander_unite()
    assert isinstance(reponse, int) and reponse >= 0
    
def test_demander_nombre_cycle(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '42')
    reponse = icc.demander_nombre_cycle()
    assert isinstance(reponse, int) and reponse >= 0
    
def test_demander_quel_dessin(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '42')
    reponse = icc.demander_quel_dessin()
    assert isinstance(reponse, int) and reponse >= 0