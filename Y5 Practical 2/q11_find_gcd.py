def find_divisor(m,n):
    p = m
    while m in range (1, n):
        if n % (p) == 0 and m % (p) == 0:
            break
        else:
            p = m - 1
    print("The greatest common divisor is " + str(p) + ".")
    
      

n1 = int(input("Enter an integer: "))
n2 = int(input("Enter another integer: "))

if n1 < n2:
    find_divisor(n1,n2)
else:
    find_divisor(n2,n1)
