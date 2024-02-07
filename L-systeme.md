# L-Systeme

## Sources

- https://fr.wikipedia.org/wiki/L-Syst%C3%A8me
- http://accromath.uqam.ca/2013/09/l-systemes-les-equations-des-plantes/

## Definition

- Une grammaire formelle, un systeme de ré-écriture
- Aristid Lindenmayer

## Systeme d'écriture formelle

Un L-système est un système de réécriture qui comprend :

- Un alphabet $V$ : l'ensemble des variables du L-système. On note $V^*$ l'ensemble des « mots » que l'on peut construire avec les symboles de $V$, et $V⁺$ l'ensemble des mots contenant au moins un symbole ;
- Un ensemble de valeur constantes $S$. Certains de ces symboles sont communs à tous les L-systèmes (voir plus bas l'interprétation en tortue) ;
- Un axiome de départ $w$ de $V⁺$, vu comme l'état initial ;
- Un ensemble de règles réécriture, noté $P$, de reproduction des symboles de $V$.

Un L-système est noté { $V$ , $S$ , $w$ , $P$ }

## La tortue

- F : Se déplacer d’un pas unitaire (∈ $V$)
---
- \+ : Tourner à gauche d’angle α (∈ $S$)
- \- : Tourner à droite d’un angle α (∈ $S$)
---
- \[ : Sauvegarder la position courante (∈ $S$)
- \] : Restaurer la dernière position sauvée (∈ $S$)
---
Pour la 3d
- & : Pivoter vers le bas d’un angle α (∈ $S$)
- ^ : Pivoter vers le haut d’un angle α (∈ $$)
- \< : Roulez vers la gauche d’un angle α (∈ $S$)
- \> : Roulez vers la droite d’un angle α (∈ $S$)
- \| : Tourner sur soi-même de 180° (∈ $S$)

## Organisation du code

- generateur.py
- test/
    - fabrication_image.py

## Explorer


```python
import generateur as g
```


```python
g.test_koch_1()
```

    F+F-F-F+F
    F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F
    F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F+F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F+F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F




