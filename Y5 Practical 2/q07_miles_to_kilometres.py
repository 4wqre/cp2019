def milestokm(miles):
    km = miles*1.609
    return "{0:.3f}".format(km)

print("Miles", "Kilometres", "Kilometres", "Miles")
for i in range(1,11):
    print(str(i), "   " , milestokm(i), "    ", str(i*5+15),"      ", "{0:.3f}".format((i*5+15)/1.609))
