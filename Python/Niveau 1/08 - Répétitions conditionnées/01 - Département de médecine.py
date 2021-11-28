populationVille = int(input())

numJour = 1
nbMalades = 1
while nbMalades < populationVille:
   numJour = numJour + 1
   nbMalades = nbMalades * 3
   
print(numJour)