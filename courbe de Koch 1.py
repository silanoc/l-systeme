import generateur as g

"""
Un L-système est noté \{V, S, \omega, P\}.
    Variable : v = {F}
    Constantes : S = {+, −}
    Axiome : w = F
    Règle : (F → F+F-F-F+F)
"""

# Initialiser
variables: list = ['F', '+', '-']
axiome : str = "F"
regle : dict = {"F" : "F+F-F-F+F"}
unite :str = 10
angle :str = 90

# Calculer les ré-éctiture souhaité
for i in range(3):
    axiome = g.reecrire(axiome, regle)
    print(axiome)

# dessiner
g.dessine(axiome, unite, angle)




