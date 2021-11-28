nbVariations = int(input())
sommePos = 0
sommeNeg = 0
for loop in range(nbVariations):
   variation = int(input())
   if variation > 0:
      sommePos = sommePos + variation
   else:
      sommeNeg = sommeNeg - variation
print(sommePos)
print(sommeNeg)