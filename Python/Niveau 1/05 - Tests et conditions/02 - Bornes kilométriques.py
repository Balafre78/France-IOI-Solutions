numéroMatin = int(input())
numéroSoir = int(input())

écart = numéroSoir - numéroMatin
if écart < 0:
   écart = -écart
print(écart)