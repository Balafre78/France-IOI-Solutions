from robot import *

haut()

# Allers-retours sur les 9 lignes du haut, pour les 8 premières colonnes
for loop in range(4):
   for loop in range(8):
      haut()
   droite()
   for loop in range(8):
      bas()
   droite()

# Deux dernières colonnes avec redescente jusqu'en bas
for loop in range(8):
   haut()
droite()
for loop in range(9):
   bas()

# Et on rentre à la position de départ
for loop in range(9):
   gauche()