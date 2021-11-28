nbPersonnes = int(input())
for loop in range(nbPersonnes):
   nbCriteres = 0
   taille = int(input())
   if (178 <= taille) and (taille <= 182):
      nbCriteres = nbCriteres + 1
   age = int(input())
   if age >= 34:
      nbCriteres = nbCriteres + 1
   poids = int(input())
   if poids < 70:
      nbCriteres = nbCriteres + 1
   aCheval = int(input())
   if aCheval == 0:
      nbCriteres = nbCriteres + 1
   aLesCheveuxBruns = int(input())
   if aLesCheveuxBruns == 1:
      nbCriteres = nbCriteres + 1
   
   if nbCriteres == 0:
      print("Impossible")
   elif nbCriteres == 5:
      print("Très probable")
   elif nbCriteres >= 3:
      print("Probable")
   else:
      print("Peu probable")