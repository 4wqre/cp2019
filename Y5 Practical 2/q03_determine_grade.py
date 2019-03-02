score = int(input("Enter score: "))

if 0 <= score <= 34:
  print("U")
elif 35 <= score <= 44:
  print("S")
elif 45 <= score <= 49:
  print("E")
elif 50 <= score <= 54:
  print("D")
elif 55 <= score <= 59:
  print("C")
elif 60 <= score <= 69:
  print("B")
elif 70 <= score <= 100:
  print("A")
else:
  print("Invalid! Score must be within 0 - 100.")
