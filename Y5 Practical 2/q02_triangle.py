a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
perimeter = a + b + c

if a + b > c and a + c > b and b + c > a:
  print("Perimeter = " + int(perimeter))
else:
  print("Invalid triangle!")
