nbPersonnes = int(input())

totalÉquipe1 = 0
totalÉquipe2 = 0
for loop in range(nbPersonnes):
   poids1 = int(input())
   poids2 = int(input())
   totalÉquipe1 = totalÉquipe1 + poids1
   totalÉquipe2 = totalÉquipe2 + poids2

if totalÉquipe1 > totalÉquipe2:
   print("L'équipe 1 a un avantage")
else:
   print("L'équipe 2 a un avantage")
   
print("Poids total pour l'équipe 1 :", totalÉquipe1)
print("Poids total pour l'équipe 2 :", totalÉquipe2)