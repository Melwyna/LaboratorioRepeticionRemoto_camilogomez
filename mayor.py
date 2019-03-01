contadorp = 0
contadorN = 0
contadorO = 0
for n in range(1, 11):
  n = int(input("ingrese el numero"))
  if (n > 0):
    contadorp += 1
  if (n < 0):
    contadorN += 1
  if (n == 0):
    contadorO += 1
print("la suma de los positivos es", contadorp)
print("la suma de negativos es", contadorN)
print("la suma de 0 es", contadorO)

