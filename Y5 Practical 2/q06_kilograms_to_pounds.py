def kgtopounds(n,end):
  print("Kilograms" + "\t" + "Pounds")
  for i in range(n,end):
    print(str(i) + "\t\t" + str("{0:.1f}".format(i*2.2)))

kgtopounds(1,10)
