nbMarchands = int(input())
minPrix = 1000 * 1000
posMinPrix = -1
pos = 1
for loop in range(nbMarchands):
   prix = int(input())
   if prix <= minPrix:
      minPrix = prix
      posMinPrix = pos
   pos = pos + 1
print(posMinPrix)