test_list = [7611529, "miles", 411.1732]
print(test_list)
test_list = [1,1,[1,2]]
print (test_list[2][1])
days =  {"sunday" : 0, "monday" : 1, "tuesday" : 2, "wednesday" : 3, "thursday" : 4, "friday" : 5, "saturday" : 6}
miss = set("Mississippi")
miss.add('X')
print(miss)
print(set([1,1,2,3]))

def sevens():
    out = ""
    for i in range(2000, 3201): #I could just itterate by 7 and check only for % 5, but I don't feel like that's the point here
        if i %7 == 0 and i % 5 != 0:
            out += str(i) + ", "
            #strings are immutable, so this will be slow, but I don't know any string builder so here we are
    return(out)
print(sevens())

def fact():
    n = int(input("Input factorial number:\n"))
    acc = 1 #accumulator
    for i in range (1, n+1):
        acc *= i
    return acc

print (fact())

def sq():
    n = int(input("Input square number:\n"))
    squares = {}
    for i in range (1, n+1):
        squares[i] = i**2
    print (squares)

sq()

def commas():
    inp = input("Input comma-separated numbers:\n")
    inp = inp.split(',')
    print (inp)
    print (tuple(inp))
commas()

class Stringy:
    s = ""
    def getString(self):
        self.s = input ("Input a string:\n")
    def printString(self):
        print(self.s.upper())

def testString():
    stringy = Stringy()
    stringy.getString()
    stringy.printString()
testString()
