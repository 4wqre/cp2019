def display_pattern(num):
    list = []
    s = 1
    list.append(s)
    for i in range (2, num+1):
        s = str(str(i) + " " + str(s))
        s = "{0:>s}".format(s)
        list.append(str(s))
    print(*list, sep="\n") #not sure how to right justify for this
    
    
n = int(input("Enter a number: ")) 
display_pattern(n)
