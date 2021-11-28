nbJours = int(input())
distanceMax = 0
for loop in range(nbJours):
   distance = int(input())
   if distance > distanceMax:
      distanceMax = distance
print(distanceMax)