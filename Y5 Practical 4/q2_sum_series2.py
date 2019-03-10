def sum_series2(i):
    if i == 0:
        return 0
    else:
        return sum_series2(i-1) + i/(2*i+1)

number = int(input("Enter a number: "))
print(sum_series2(number))
