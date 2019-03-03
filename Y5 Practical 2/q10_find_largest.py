n = 10

while n < 12000 ** (1/3):
  if n**3 < 12000:
    n = n + 1
  else:
    break

print("The largest integer n such that n3 is less than 12,000 is " + str(int(n-1))+ ".")
