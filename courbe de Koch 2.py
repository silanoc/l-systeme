import generateur as g
import turtle as t

"""
    F : Se déplacer d’un pas unitaire (∈ V)
    + : Tourner à gauche d’angle α (∈ S)
    - : Tourner à droite d’un angle α (∈ S)
    & : Pivoter vers le bas d’un angle α (∈ S)
    ^ : Pivoter vers le haut d’un angle α (∈ S)
    < : Roulez vers la gauche d’un angle α (∈ S)
    > : Roulez vers la droite d’un angle α (∈ S)
    | : Tourner sur soi-même de 180 ° (∈ S)
    [ : Sauvegarder la position courante (∈ S)
    ] : Restaurer la dernière position sauvée (∈ S)

Un L-système est une grammaire formelle qui comprend :

    Un alphabet V : l'ensemble des variables du L-système. V^* est l'ensemble des « mots » que l'on peut construire avec les symboles de V, et V^+ l'ensemble des mots contenant au moins un symbole.
    Un ensemble de valeur constantes S. Certains de ces symboles sont communs à tous les L-système (voir plus bas la Turtle interpretation).
    Un axiome de départ \omega choisi parmi V^+, c'est-à-dire l'état initial.
    Un ensemble de règles, noté P, de reproduction des symboles de V.




"""

# Initialiser
variables: list = ['F', '+', '-']
axiome : str = "F"
regle : dict = {"F" : "F+F-F-FF+F+F-F"}
unite :str = 500
    

print(axiome)
t.pencolor('grey')
g.dessine(axiome, unite)


axiome = g.reecrire(axiome, regle)
unite=unite/4
print(axiome)
t.pencolor('black')
t.penup()
t.home()
t.pendown()
g.dessine(axiome, unite)


axiome = g.reecrire(axiome, regle)
unite=unite/4
print(regle)
t.pencolor('red')
t.penup()
t.home()
t.pendown()
g.dessine(axiome, unite)

axiome = g.reecrire(axiome, regle)
unite=unite/4
print(regle)
t.pencolor('green')
t.penup()
t.home()
t.pendown()
g.dessine(axiome, unite)

axiome = g.reecrire(axiome, regle)
unite=unite/4
print(regle)
t.pencolor('blue')
t.penup()
t.home()
t.pendown()
g.dessine(axiome, unite)
