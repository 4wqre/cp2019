import math
def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False

    x = 3
    while x < math.sqrt(n)+1:
        if n%x == 0:
            return False
        x = x + 2
    return True
        
list = []
n = 2
m = 0
while m < 100:
    while len(list)<10:
        if is_prime(n) is True:
            list.append(n)
            n = n + 1
        else:
            n = n + 1
    print(*list, sep=" ")
    m = m + 1
    list = [ ]
    
