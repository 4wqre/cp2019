#function m_series
def m_series(i):
    x = 1
    n = 0
    while x in range (1,i+1):
        n = n + x/(x+1)
        x = x + 1 
    return n 

#table
n = 1
table = {}
header1 = "i"
header2 = "\t" + "m(i)"
table[header1] = header2
while n in range (0, 21):
    num = str(n)
    output = "\t" + "{0:.4f}".format(m_series(n))
    table[num] = output
    n = n + 1

for key, value in table.items():
    print(key, value)
