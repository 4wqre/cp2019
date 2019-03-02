year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 != 00:
  print("Leap")
elif year % 400 == 0:
  print("Leap")
else:
  print("Non-leap")
