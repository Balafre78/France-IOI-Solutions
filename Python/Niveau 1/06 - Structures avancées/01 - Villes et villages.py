nbLieux = int(input())
nbVilles = 0
for loop in range(nbLieux):
   population = int(input())
   if population > 10 * 1000:
      nbVilles = nbVilles + 1
print(nbVilles)