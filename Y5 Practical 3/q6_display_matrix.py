import random
number = int(input("Enter a number: "))
for j in range(number):
    for i in range(number):
        print(random.randint(0,1), end=" ")
    print()
