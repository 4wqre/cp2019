def sum_digits(i):
    if i/10 == 0:
        return i
    else:
        return i%10 + sum_digits(int(i/10)) 

num = int(input("Enter a number :"))
print(sum_digits(num))
