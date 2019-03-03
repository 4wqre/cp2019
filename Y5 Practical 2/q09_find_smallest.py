import math
n = math.sqrt(12000)

while n > 0:
  if n*n > 12000:
    break
  else:
      n = n + 1

print("The smallest integer n such that n^2 is greater than 12,000 is " + str(int(n+1)) + ".")
