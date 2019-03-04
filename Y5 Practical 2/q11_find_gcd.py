def find_divisor(m,n):
    while m in range (1, n):
        if n % (m) == 0 and m % (m) == 0:
            break
        else:
            m = m - 1
    print("The greatest common divisor is " + str(m) + ".")
    
      

n1 = int(input("Enter an integer: "))
n2 = int(input("Enter another integer: "))

if n1 < n2:
    find_divisor(n1,n2)
else:
    find_divisor(n2,n1)
