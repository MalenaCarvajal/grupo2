from math import sqrt
A = float(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = float(input("Ingrese el coeficiente de la variable lineal\n"))
C = float(input("Ingrese el término independiente\n"))
x1= 0
x2= 0
if ((B**2)-4*A*C) < 0:
  print("La ecuación no tiene soluciones reales")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
  print(x1)
  print(x2)
  
  