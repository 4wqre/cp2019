num = int(input("Enter an integer: "))
def reverse_int(n):
    m = 0
    while n > 0:
        remainder = n % 10
        n = n // 10
        m = (m*10) + remainder
    return m

print(reverse_int(num))
