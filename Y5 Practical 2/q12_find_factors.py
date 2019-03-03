def find_smallest_factors(n):
    factors = []
    m = 2
    while n > 1 and m < n:
        for i in range (1,int(n)):
            if n % m == 0:
                factors.append(m)
                m = m
                n = n/m
            else:
                m = m + 1 
    print(factors)

input = int(input("Enter an integer: "))
find_smallest_factors(input)
