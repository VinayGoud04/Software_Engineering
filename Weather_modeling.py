import math

with open("Exp-1_SE.txt", "r") as file:
    line = file.readline()
    a,b,c = map(float, line.split())

discriminant = b**2 - 4*a*c
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots are: {root1:.2f}, {root2:.2f}")
else:
    print("No real roots")

temperature = root1 if discriminant >= 0 else None
if temperature:
    print(f"Modeled Temperature: {temperature:.2f}°C")



Roots are: 2.00, 1.00
Modeled Temperature: 2.00°C
