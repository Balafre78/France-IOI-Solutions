positionDépart = int(input())
largeurEmplacement = int(input())
nbVendeurs = int(input())

position = positionDépart
for iVendeur in range(nbVendeurs + 1):
   print(position)
   position = position + largeurEmplacement