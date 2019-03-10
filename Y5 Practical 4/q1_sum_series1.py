def sum_series1(i):
    if i == 0:
        return 0
    else:
        return sum_series1(i-1) + 1/i

number = int(input("Please enter a number: "))
print(sum_series1(number))
