import math

print("50 + 50 = {:d}".format(50 + 50))
print("30+*6,6^6,6**6,6+6+6+6+6+6 is invalid syntax")
print("Hello World\nHello World : 10")


i = input("Please enter principle in dollars, rate in percent per year, and period in months\n")
l = i.split()
p = int(l[0])
r = int(l[1])
r = r*0.01/12
n = int(l[2])
a = (p*r*(1+r)**n)/((1+r)**n-1)
a = math.ceil(a)
print (a)