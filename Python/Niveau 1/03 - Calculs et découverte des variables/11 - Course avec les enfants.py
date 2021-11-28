from robot import *

anneau = 1
for loop in range(10):
   for loop in range(anneau):
      droite()
   ramasser()
   for loop in range(anneau):
      gauche()  
   deposer()
   anneau = anneau + 1