# L-Système

- Date :
    - Projet commencé en 2015, sûrement 1 des premiers après avoir programmé en squeak.
    - Reprise en février 2024
- Autaire : Silanoc
- Version : 1.0

## Objectif

Programme pour tracer des courbes de type L-système.
Lire le doc L-systeme.md pour les explications.

Les dessins sont tracés par le module turtle de python.

## Pour utiliser le programme

Pour lancer le programme faire `python run.py`
Cela revient à lancer python `interface.console_affichage.py`

On peut lancer individuellement chacun des fichiers de bestiaire.

## Architecture

- bestiaire
    |- plusieurs fichiers pouvant etre exécuté et servant à intialiser des dessins
    |
- domaine
    |- generateur.py : le fichier principale
- image Fractale
    |- des images d'archives de 2015
- interface
    |- console_affichage
    |- console_commande.py 
- tests
- L-système.md
- README.md
- requierement.txt
- run.py : pour lancer directement

    