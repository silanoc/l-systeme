# Méthodologie des tests pour le projet L-Systeme

- autair : Silanoc
- date : 2024-02-06

## Typage avec mypy

tester un fichier

`mypy generateur.py`

tester tous les fichiers

`mypy *.py`

`mypy --check-untyped-defs *.py`

`mypy *.py ./bestiaire/*.py ./tests/*.py`

## Tester les fonctions avec pytest

`pytest -v`
`pytest -v tests_avec_pytest.py`

### Ré-écrire

Plusieurs exemples existent sur internet, dont wikipédia.
En faisant confiance en ces sources, on peut obtenir des séquences fiables pour les comparaisons.

### Dessiner

Le test se fait en comparant une image de référence �  celle fabriquée lors du test.

Le test utilise ``list(image.getdata()) de la librairie Pillow. On compare tous les pixels des deux images.

Les images de tests sont produite en python avec turtel, dans le fichier fabrique_images.py

Idem, les images sont fabriqué �  partir d'exemple de wikipédia ou autre sources jugées fiable.'