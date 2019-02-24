number = int(input("Enter a number between 0 and 1000: "))

ones = int(number % 10)

number_without_ones = int(number // 10)
tens = int(number_without_ones % 10)

number_with_hundreds_only = int(number_without_ones // 10)
hundreds = int(number_with_hundreds_only % 10)

print("Sum of all digits: ", str(ones + tens + hundreds))
