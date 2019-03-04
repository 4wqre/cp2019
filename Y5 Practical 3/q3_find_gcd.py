def gcd(m,n):
    if m > n:
        x = n
        while x in range (1,n+1):
            if m % x == 0 and n % x == 0:
                break
            else:
                x = x-1
        print("The greatest common divisor of " + str(m) + " and " + str(n) + " is " + str(x) + ".")

    elif n > m:
        x = m
        while x in range (1,m+1):
            if m % x == 0 and n % x == 0:
                break
            else:
                x = x-1
        print("The greatest common divisor of " + str(m) + " and " + str(n) + " is " + str(x) + ".")

    else:
        print("The greatest common divisor of " + str(m) + " and " + str(n) + " is " + str(m) + ".")
        
gcd(24,16)
gcd(255,25)
