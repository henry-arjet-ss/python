names = ["Grant", "Sherman", "Meade", "McClellen"]

def crowd(names):
    if len(names) > 3:
        print("SOCAIL DISTANCE! IT'S TOO CROWDED IN HERE!")
    else: print ("Ok, but y'all better stay six feet apart")


crowd(names)
names.pop()
names.pop()
crowd(names)

def crowd2(names):
    if len(names) > 5 :
        print("Is anyone else worried about their kneecaps? 'Cause there's a mob in here")
    elif len(names) > 2:
        print("Two's a party, but three is a crowd. So are four and five.")
    elif len(names) > 0: 
        print ("Pretty lonely here")
    else: 
        print ("*crickets*")

names2 = ["Washington", "Lafayette", "Gates", "Hamilton", "Knox", "Arnold"]

crowd2(names2)

names2.pop() #Get rid of the traitor first. We would have had Canada if it wasn't for his ego
names2.pop()
crowd2(names2)

names2.pop()
names2.pop()
crowd2(names2)

names2.pop()
names2.pop()
crowd2(names2)

