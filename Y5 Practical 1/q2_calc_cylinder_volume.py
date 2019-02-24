radius = float(input("Radius of base: "))
length = float(input("Length of cylinder: "))

import math
area = float(radius * length * math.pi)
volume = float(area * length)

print(volume)
