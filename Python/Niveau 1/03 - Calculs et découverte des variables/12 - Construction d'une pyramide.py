nbCubes = 0
largeurArête = 1
for loop in range(9):
   nbCubes = nbCubes + largeurArête * largeurArête * largeurArête
   largeurArête = largeurArête + 2
print(nbCubes)