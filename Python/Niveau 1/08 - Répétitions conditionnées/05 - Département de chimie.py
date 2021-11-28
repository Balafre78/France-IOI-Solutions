nbMesures = int(input())
tempMin = int(input())
tempMax = int(input())

numMesure = 0
tempValide = True
while numMesure < nbMesures and tempValide:
   température = int(input())
   tempValide = (tempMin <= température and température <= tempMax)
   if tempValide:
      print("Rien à signaler")
   else:
      print("Alerte !!")
   numMesure = numMesure + 1