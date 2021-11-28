posActuelle = int(input())
nbVillages = int(input())
nbAccessibles = 0
for loop in range(nbVillages):
   posVillage = int(input())
   ecart = posActuelle - posVillage
   if ecart < 0:
      ecart = -ecart
   if ecart <= 50:
      nbAccessibles = nbAccessibles + 1
print(nbAccessibles)