aDeviner = int(input())
proposition = int(input())
nbEssais = 1
while proposition != aDeviner:
   if proposition < aDeviner:
      print("c'est plus")
   if proposition > aDeviner:
      print("c'est moins")
   proposition = int(input())
   nbEssais = nbEssais + 1
print("Nombre d'essais nécessaires : ")
print(nbEssais)