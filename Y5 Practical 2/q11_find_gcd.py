
def find_divisor(m,n):
    x = m
    while x in range (1, m+1):
        if n%x == 0 and m%x == 0:
            break
        else:
            x = x - 1
    print("The greatest common divisor is " + str(x) + ".")
     

n1 = int(input("Enter an integer: "))
n2 = int(input("Enter another integer: "))

if n1 < n2:
    find_divisor(n1,n2)
else:
    find_divisor(n2,n1)
