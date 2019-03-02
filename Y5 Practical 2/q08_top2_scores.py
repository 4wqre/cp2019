list = {}
choice = input("Are there any more entries? (Y/N): ")

while choice == "Y" or choice == "y":
    name = input("Enter student's name: ")
    score = input("Enter score: ")
    list[score] = name
    choice = input("Are there any more entries? (Y/N): ")
    if choice == "Y" or choice == "y":
        True
    else:
        break
#if user types less than one entry
else:
    choice = input("Are there any more entries? (Y/N): ")
    while choice == "Y" or choice == "y":
            name = input("Enter student's name: ")
            score = input("Enter score: ")
            list[score] = name
            choice = input("Are there any more entries? (Y/N): ")
            if choice == "Y" or choice == "y":
                True
            else:
                break

print(list[max(list.keys())] + " got the highest score, " + max(list.keys()) + "." )
del list[max(list.keys())]
print(list[max(list.keys())] + " got the second highest score, " + max(list.keys()) + ".")
