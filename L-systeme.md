# L-Systeme

## Sources

- https://fr.wikipedia.org/wiki/L-Syst%C3%A8me
- https://fr.wikipedia.org/wiki/Flocon_de_Koch
- http://accromath.uqam.ca/2013/09/l-systemes-les-equations-des-plantes/

## Concepts de bases

### Definition

- Une grammaire formelle, un systeme de ré-écriture
- Aristid Lindenmayer

### Systeme d'écriture formelle

Un L-système est un système de réécriture qui comprend :

- Un alphabet $V$ : l'ensemble des variables du L-système. 
    - On note $V^*$ l'ensemble des « mots » que l'on peut construire avec les symboles de $V$
    - $V⁺$ l'ensemble des mots contenant au moins un symbole ;
- Un ensemble de valeur constantes $S$. Certains de ces symboles sont communs à tous les L-systèmes (voir plus bas l'interprétation en tortue) ;
- Un axiome de départ $w$ de $V⁺$, vu comme l'état initial ;
- Un ensemble de règles réécriture, noté $P$, de reproduction des symboles de $V$.

Un L-système est noté { $V$ , $S$ , $w$ , $P$ }

### La tortue

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

### D0L-système ou Deterministic 0-context System

Indépendant du contexte, donne toujours la même chose.

#### Courbes, fractales géométriques

terme à améliorer.

##### Courbe de Koch triangle

- Variable : $v$ = {F}
- Constantes : $S$ = {+, −}
- Axiome : $w$ = F
- Règle : $p$ = (F → F+F-F+F)

##### Flocon de Koch

- Variable : $v$ = {F}
- Constantes : $S$ = {+, −}
- Axiome : $w$ = F--F--F
- Règle : $p$ (F → F+F-F+F)

##### Courbe quadratique de Koch (type 1)

- Variable : $V$ = {F}
- Constantes : $S$ = {+, −}
- Axiome : $w$ = F
- Règle : $P$ = (F → F+F−F−F+F)

voir courbe_quadratique_de_Koch_type_1.py

##### Courbe quadratique de Koch (type 2)

- Variable : $V$ = {F}
- Constantes : $S$ = {+, −}
- Axiome : $w$ = F
- Règle : $P$ = (F → F+F-F-FF+F+F-F)

voir courbe_quadratique_de_Koch_type_2.py

#### plantes, arbres...

##### arbre de base

Le plus simple trouvé sur internet 
https://accromath.uqam.ca/2013/09/l-systemes-les-equations-des-plantes/


- Variable : $V$ = {F, S}
- Constantes : $S$ = {+, −, \[\, \]}
- Axiome : $w$ = F
- Règle : $P$ = (F → S\[-F\]+[+F])

F : branche Fertile (tortue avance en vert)
S : branche stérile (tortue avance en marron)

Pour le moment pas de couleur prise en charge, donc F -> F\[-F\]+[+F]

voir plante_1.py

#### plante 1

source : https://fr.wikipedia.org/wiki/L-Syst%C3%A8me#Exemple_d'un_D0L-syst%C3%A8me

Plante
{
angle 20
axiom X
X=F[+X]F[−X]+X
F=FF
}

F autorise la tortue à se déplacer, pas X qui conte comme "rien"

voir plante_1.py


#### plante 2

source : https://en.wikipedia.org/wiki/L-system#Example_7:_fractal_plant

- alphabet = ['F', 'X']
- variables = ['+', '-', '[', ']']
- axiome = "X"
- regles = {"X" : "F+[[X]-X]-F[-FX]+X", "F" : "FF"}

voir plante_2.py








