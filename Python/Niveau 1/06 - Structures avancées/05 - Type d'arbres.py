hauteur = int(input())
nbFolioles = int(input())
if hauteur < 9:
   if nbFolioles > 6:
      print("Tinuviel")
   else:
      print("Falarion")
else:
   if nbFolioles < 8:
      print("Dorthonion")
   else:
      print("Calaelen")