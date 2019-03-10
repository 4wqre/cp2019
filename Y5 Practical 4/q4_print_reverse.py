def reverse_int(i):
    if i/10 == 0:
        return i
    else:
        return str(i%10) + str(reverse_int(int(i/10))) #not sure how to remove the 0 at the end

num = int(input("Enter a number :"))
print(reverse_int(num))
