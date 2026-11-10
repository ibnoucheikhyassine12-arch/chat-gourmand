# Chat gourmand

Jeu Pygame : le chat attrape les poissons (+100 points) et évite les bombes (-1 vie, 3 vies au total). Le jeu accélère à chaque poisson.

## Installation
pip install -r requirements.txt

## Lancer le jeu
python main.py

## Comment jouer
- ESPACE : commencer
- Flèches gauche / droite : déplacer le chat
- ECHAP : retour à l'accueil
- ENTREE : rejouer après Game Over

## Meilleur score
Les scores sont enregistrés dans une base SQLite (chat_gourmand_v2.db). Le meilleur score s'affiche à l'accueil et en jeu.