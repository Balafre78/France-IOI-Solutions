nombreMaximumPierres = int(input())
nombrePierres = 0
hauteur = 1
while nombrePierres + hauteur * hauteur <= nombreMaximumPierres:
   nombrePierres = nombrePierres + hauteur * hauteur
   hauteur = hauteur + 1  
print(hauteur - 1)
print(nombrePierres)