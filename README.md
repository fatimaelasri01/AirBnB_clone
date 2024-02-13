# AirBnB_clone
<img src="hbnb.png" width=100%>

## Description

Ce projet, appelé "The Room SE", est un projet de groupe visant à éclairer les étudiants en génie logiciel sur les aspects détaillés du développement complet d'une application web en reproduisant le site/web app Airbnb.

## Table des matières
 * [Description](#Description)
 * [Utilisation](#Utilisation)
 * [Description des Fichiers](#Description-des-Fichiers)
 * [Bugs](#Bugs)
 * [Auteur](#Auteur)

## Utilisation
Pour utiliser cette application :
 - Clonez ce dépôt ``git clone https://github.com/StephenMakenziWaweru/AirBnB_clone``
 - Accédez-y et rendez le fichier console.py exécutable ``cd AirBnB_clone; chmod u+x console.py``
 - Consultez les commandes ci-dessous pour plus d'aide

| Commande | Description |
| --- | --- |
| `./console.py` | Ouvre l'interpréteur `(hbnb)` |
|  `all` | Affiche toutes les représentations en chaîne de toutes les instances |
| `create` | Crée une nouvelle instance de BaseModel |
| `destroy` | Supprime une instance basée sur le nom de la classe et l'identifiant |
| `show` | Affiche la représentation en chaîne d'une instance |
| `update` | Met à jour une instance basée sur le nom de la classe et l'identifiant |
| `quit` | Commande QUIT qui quitte le programme |

### Exemple d'utilisation
Lancement de console.py, vérification des commandes disponibles et création d'un utilisateur
## Description des Fichiers

| Fichier | Description |
| :--- | :--- |
| `console.py` | Crée l'interpréteur de ligne de commande |
| `models/base_model.py` | Contient une classe définissant les attributs et méthodes pour d'autres classes |
| `models/engine/file_storage.py` | Contient la classe pour la sérialisation et la désérialisation JSON |
| `tests/test_console.py` | Cas limites pour l'interface en ligne de commande |
| `tests/test_base_model.py` | Cas limites pour BaseModel() |
| `tests/test_file_storage.py` | Cas limites pour FileStorage() |

## Bugs
- Pas de bugs connus

## Auteur
Fatima EL ASRI <fatimaelassri041@gmail.com>
