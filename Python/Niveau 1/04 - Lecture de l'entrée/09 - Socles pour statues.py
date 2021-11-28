largeurBas = int(input())
largeurHaut = int(input())
 
volume = 0
largeur = largeurHaut
for loop in range(largeurBas - largeurHaut + 1):
   volume = volume + largeur * largeur
   largeur = largeur + 1
 
print(volume)