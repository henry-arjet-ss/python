#Tonight I'm gonna have myself a real good time
#I feel alive

import random

#And the world I'll turn it inside out, yeah
#I'm floating around in ecstasy



def sevens(): #I just did this in 2_b
    out = ""
    for i in range(1500, 2701): 
        if i %7 == 0 and i % 5 == 0:
            out += str(i) + ", "
    return(out)
#print(sevens())

#So, don't stop me now
#'Cause I'm having a good time, having a good time

def c_and_f(inp): #Takes a string containing a number and a letter, either f or c
    inp = inp.split()
    n = float(inp[0])
    #I'm a shooting star leaping through the sky
    #Like a tiger defying the laws of gravity

    if inp[1].upper() == "F": #fahrenheit to celsius
        o = (n - 32)*5/9
        o = round(o)
        print (str(n) + "°F is " + str(o) + " in Celsius")
        #I'm a racing car passing by like Lady Godiva
    else:
        o = n*9/5 + 32
        o = round(o)
        print (str(n) + "°C is " + str(o) + " in Fahrenheit")
        #I'm gonna go, go, go
        #There's no stopping me

#I'm burning through the sky, yeah
c_and_f("200 f") #Two-hundred degrees
#That's why they call me Mr. Fahrenheit
c_and_f("93.3 c")
#I'm traveling at the speed of light, I wanna make a supersonic man out of you

def guesses():
    ans = random.randint(1, 9)
    while (1):
        i = input("Guess a number between 1 and 9: ")
        if int(i) == ans:
            print("Well guessed!")
            return
        else:
            print("Please guess again\n")    
            
#guesses()

def stars():
    for i in range(1, 6):
        s = ""
        for j in range(1, i+1):
            #print (str(i) + ", " + str(j))
            s+="*"
        print (s)
    for i in range(4, 0, -1):
        s = ""
        for j in range(1, i+1):
            #print (str(i) + ", " + str(j))
            s+="*"
        print (s)
#stars()

def reverse():
    inp = input("Please enter a word to reverse: ")
    o = ""
    for i in range (len(inp)-1, -1, -1):
        o+=inp[i]
    print (o)
#reverse()

def counter(inp):
    eacc = 0 #even accumulator
    oacc = 0
    for i in inp:
        if i % 2 == 0:
            eacc+=1 
        else:
            oacc+=1
    print("Number of even numbers: " + str(eacc))
    print("Number of odd numbers: " + str(oacc))

counter((1,2,3,4,5,6,7,8,9))

def list_printer(inp):
    for i in inp:
        print(str(type(i)) + ": " + str(i))
list_printer([1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}])

for i in range (0,6):
    if i % 3 == 0 and i != 0:
        continue
    print (i)